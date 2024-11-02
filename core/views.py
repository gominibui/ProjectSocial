# core/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required()  # URL для регистрации
def main(request):
    # Перенаправление на уникальную страницу пользователя
    return render(request,'base.html')

@login_required()  # URL для регистрации
def user_main(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Получаем пользователя или 404
    return render(request, 'base.html', {'user': user})  # Передаем пользователя в шаблон