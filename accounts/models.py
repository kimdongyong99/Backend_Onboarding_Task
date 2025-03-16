from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=30, unique=True)
    refresh_token = models.TextField(blank=True, null=True)  # Refresh Token 저장

    # 기본 username 필드 제한을 완화(공백 허용)
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.username
