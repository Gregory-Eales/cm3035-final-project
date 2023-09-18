import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from django.contrib.auth.models import User
from channels.db import database_sync_to_async


"""
i can make sure the user is authed and get their username by doing this:



"""

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        # really we should be creating the connection by using the user's id
        # and the other user's id to get a conversation id.
        # if the converstaion does not exist, create it
        # then add the user to the group

        self.chat_name = self.scope['url_route']['kwargs']['room_name']

        # split by - intwo two user ids
        user_ids = self.chat_name.split('-')

        print(user_ids)
        

        # if the current user is not in this list then return an error
        if str(self.scope['user'].id) not in user_ids:
            await self.close()

        self.room_group_name = 'chat_%s' % self.chat_name
        self.chat_name = self.scope['url_route']['kwargs']['room_name']

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        self.send(text_data=json.dumps({
            'message': 'hello world'
        }))

    async def disconnect(self, close_code):
            
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # make an async call to the database to get the user
        try:
            # get username of the current user
            user = await database_sync_to_async(User.objects.get)(id=self.scope['user'].id)
            username = user.username

        # handle exception and print error
        except Exception as e:
            print("-"*80)
            print("error: ", e)
            print("-"*80)
            username = 'anonymous'


        print('-'*80)
        print("user sent message: ", message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    async def chat_message(self, event):

        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'message': "{}: {}".format(username, message)
        }))