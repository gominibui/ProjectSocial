# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Кастомная модель пользователя, расширяющая стандартную."""
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    """Модель профиля пользователя для хранения дополнительных данных."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"




