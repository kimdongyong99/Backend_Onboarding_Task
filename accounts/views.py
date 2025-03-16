from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


class SignupView(APIView):
    def post(self, request):
        # 요청 데이터를 Serializer에 전달
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            # 유저 생성
            user = serializer.save()
            # 성공 응답
            return Response({
                "username": user.username,
                "nickname": user.nickname,
                "roles": [{"role": "USER"}]
            }, status=status.HTTP_201_CREATED)
        # 유효하지 않은 데이터 응답
        return Response({"error": "Invalid input data", "details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # 사용자 인증
        user = authenticate(username=username, password=password)
        if user:
            # JWT 토큰 발급
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Refresh Token을 서버(DB)에 저장
            user.refresh_token = str(refresh)
            user.save()

            return Response({
                "access_token": access_token
            }, status=status.HTTP_200_OK)

        # 인증 실패
        return Response({"error": "Incorrect username or password"}, status=status.HTTP_401_UNAUTHORIZED)



class TokenRefreshView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        try:
            # Refresh Token으로 사용자 찾기
            user = User.objects.get(refresh_token=refresh_token)
            refresh = RefreshToken(refresh_token)

            # 새로운 Access Token 생성
            return Response({
                "access_token": str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Invalid refresh token"}, status=status.HTTP_401_UNAUTHORIZED)