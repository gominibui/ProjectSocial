# core/urls.py

from django.urls import path
from .views import main


urlpatterns = [
    path('', main, name='main'),  # Главная страница (или редирект на регистрацию) # Уникальная главная страница для пользователя
]
