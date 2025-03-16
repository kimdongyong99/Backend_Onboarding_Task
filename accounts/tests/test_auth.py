from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
import pytest

User = get_user_model()  # 현재 프로젝트의 User 모델 가져오기

@pytest.mark.django_db
def test_signup_success():
    client = APIClient()
    response = client.post('/accounts/signup/', {
        "username": "testuser",
        "password": "testpassword123",
        "nickname": "tester"
    })
    assert response.status_code == 201
    assert response.data['username'] == "testuser"
    assert response.data['nickname'] == "tester"

@pytest.mark.django_db
def test_login_success():
    client = APIClient()
    # 사용자 생성
    User.objects.create_user(username="testuser", password="testpassword123")
    response = client.post('/accounts/login/', {
        "username": "testuser",
        "password": "testpassword123"
    })
    assert response.status_code == 200
    assert "access_token" in response.data

@pytest.mark.django_db
def test_login_failure():
    client = APIClient()
    response = client.post('/accounts/login/', {
        "username": "wronguser",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert "error" in response.data

@pytest.mark.django_db
def test_token_refresh():
    client = APIClient()
    # 사용자 생성 및 토큰 발급
    user = User.objects.create_user(username="testuser", password="testpassword123")
    refresh = RefreshToken.for_user(user)
    user.refresh_token = str(refresh)
    user.save()

    # 갱신 요청
    response = client.post('/accounts/token/refresh/', {
        "refresh_token": str(refresh)
    })
    assert response.status_code == 200
    assert "access_token" in response.data