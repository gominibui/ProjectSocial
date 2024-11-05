# core/urls.py

from django.urls import path
from .views import main

app_name = 'core'
urlpatterns = [
    path('', main, name='main'),  # Главная страница (или редирект на регистрацию) # Уникальная главная страница для пользователя
]
