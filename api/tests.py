from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import Image, Post, Friend  # replace 'core' with your app name if different

# class UserViewSetTestCase(APITestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username='test', password='test')
#         self.client.login(username='test', password='test')

#     def test_user_list(self):
#         url = reverse('user-list')  # Replace with the actual name of the URL
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

# # Similar test cases for ImageViewSet, PostViewSet, and FriendViewSet

# class ImageViewSetTestCase(APITestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username='test', password='test')
#         self.image = Image.objects.create(user=self.user, 
#         self.client.login(username='test', password='test')

#     def test_image_list(self):
#         url = reverse('image-list')  # Replace with the actual name of the URL
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

# class PostViewSetTestCase(APITestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username='test', password='test')
#         self.post = Post.objects.create(user=self.user, 
#         self.client.login(username='test', password='test')

#     def test_post_list(self):
#         url = reverse('post-list')  # Replace with the actual name of the URL
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

# class FriendViewSetTestCase(APITestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username='test', password='test')
#         self.friend = Friend.objects.create(friender=self.user, ...)  # Fill in with other required fields
#         self.client.login(username='test', password='test')

#     def test_friend_list(self):
#         url = reverse('friend-list')  # Replace with the actual name of the URL
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
