from django.urls import path
from .views import login_view, register_view, logout_view, home, profile_view, chat_view, search_view, image_view, create_post, add_friend
from . import api

urlpatterns = [
    path('', home, name='home'),
    path('register', register_view, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('profile/<str:username>/', profile_view, name='profile'),
    path('chat', chat_view, name='chat'),
    path('chat/<int:friend_id>/', chat_view, name='chat'),
    path('search', search_view, name='search'),
    path('api/image/', image_view, name="image_api"), 
    path('api/images/', api.ImageList.as_view(), name="image_api"),
    path('api/posts/', create_post, name="post_api"),
    path('api/friends/', add_friend, name="friend_api"),
]

