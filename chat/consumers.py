import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import Message
from asgiref.sync import sync_to_async
import asyncio

class ChatRoomConsumer(AsyncWebsocketConsumer):
    @sync_to_async
    def fetch_messages(self, data):
        print("fetching")
        messages = Message.last_10_msgs()
        # json_ser = asyncio.run(self.messages_to_json(messages))
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        asyncio.run(self.send_message(content))
        # return self.send_message(content)
    @sync_to_async
    def new_message(self, data):
        username = data['from']
        user = User.objects.get(username=username)
        message = Message(author=user,
            content=data['message'])
            
        message.save()
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)
    @sync_to_async
    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result
    @sync_to_async
    def message_to_json(self, message):
        return {
            'id': message.id,
            'author': message.author.username,
            'content': message.content,
            'timestamp': str(message.date_posted)
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    @sync_to_async
    def get_users(self,username,message):
        user = User.objects.get(username=username)
        msg1 = Message(content=message,author=user)
        msg1.save()
        msgs = Message.objects.all()
        # for i in msgs:
        #     print(i.content)
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        await self.commands[data['command']](self, data)

    async def send_chat_message(self,message):
        # message = text_data_json['message']
        # username = text_data_json['username']
        # await self.get_users(username,message)
        print("sending")
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message
            }
        )
    async def send_message(self, message):
        await self.send(text_data=json.dumps(message))

    async def chatroom_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps(message))

