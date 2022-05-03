import json

from channels.generic.websocket import AsyncWebsocketConsumer

class CallConnection(AsyncWebsocketConsumer):
    async def connect(self):
        room_name = 'testing'
        print(room_name)
        self.group_name=room_name
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()


    async def disconnect(self, code):
        pass

    async def receive(self, text_data,type='receive'):
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'processingCenter',
                'value': text_data,
            }
        )

    async def processingCenter(self, event):

            data=event['value']
            print(data)
            await self.send(data)

