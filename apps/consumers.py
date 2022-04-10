from channels.generic.websocket import JsonWebsocketConsumer
from apps.models import Chat,ChatGroup
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User

class MySyncConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.group = self.scope['url_route']['kwargs']['group_name']
        print(self.group)
        async_to_sync(self.channel_layer.group_add)(self.group,self.channel_name)
        self.accept()
    
    def receive_json(self, content):
        group_name = ChatGroup.objects.get(name=self.group)
        if self.scope['user'].is_authenticated:
            user_name = str(self.scope['user'])
            user = User.objects.get(username=user_name)
            content['user'] = user_name
            print(content)
            chat = Chat(
                content=content['message'],
                user=user,
                group=group_name
            )
            chat.save()
            async_to_sync(self.channel_layer.group_send)(self.group,{
                'type':'chat.message',
                'text':content
            })
        else:
            pass
        # self.send_json(content)
    def chat_message(self,event):
        print(event['text'])
        self.send_json(content=event['text'])

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(self.group,self.channel_name)