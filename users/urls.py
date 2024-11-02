from django.urls import path
from .views import RegisterView, LoginView, ProfileView, EditProfileView

app_name = 'users'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('edit-profile/', EditProfileView.as_view(), name='edit_profile'),
]
