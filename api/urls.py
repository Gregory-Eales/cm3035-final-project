from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'friends', views.FriendViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
