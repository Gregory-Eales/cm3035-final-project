from django.urls import path
from .views import login_view, register_view, logout_view, home, profile_view, chat_view

urlpatterns = [
    path('', home, name='home'),
    path('register', register_view, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('profile', profile_view, name='profile'),
    path('chat', chat_view, name='chat'),
]