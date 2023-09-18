from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # chats should be chatty/ws/1-2/ user_ids sperated by a dash
    re_path(r'chatty/ws/(?P<room_name>[\w-]+)/$', consumers.ChatConsumer.as_asgi()),
]