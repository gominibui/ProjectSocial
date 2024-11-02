# users/views.py

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserEditForm


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registrer.html', {'form': form})  # Исправлено название шаблона

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:main')  # Исправлено на 'core:main'
        return render(request, 'registrer.html', {'form': form})  # Исправлено название шаблона

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:main')  # Исправлено на 'core:main'
        return render(request, 'login.html', {'error': 'Invalid username or password'})

class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html', {'user': request.user})

class EditProfileView(View):
    def get(self, request):
        form = UserEditForm(instance=request.user)
        return render(request, 'edit_profile.html', {'form': form})

    def post(self, request):
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')  # Перенаправление на страницу профиля
        return render(request, 'edit_profile.html', {'form': form})