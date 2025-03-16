from rest_framework import serializers
from .models import User

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'nickname']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_username(self, value):
        # 연속된 공백을 방지
        if "  " in value:
            raise serializers.ValidationError("Username cannot contain multiple consecutive spaces.")
        return value