# core/urls.py

from django.urls import path
from .views import main, user_main

urlpatterns = [
    path('', main, name='main'),  # Главная страница (или редирект на регистрацию)
    path('user/<int:user_id>/', user_main, name='user_main'),  # Уникальная главная страница для пользователя
]
