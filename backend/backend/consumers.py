import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from datetime import datetime
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from datetime import datetime

class BalanceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope["url_route"]["kwargs"]["user_id"]
        print(f"User {self.user_id} connected")
        await self.accept()

    async def disconnect(self, close_code):
        print(f"User {self.user_id} disconnected with close code {close_code}")
        from mainapp.models import TelegramUser
        try:
            user = await self.get_user(TelegramUser, self.user_id)
            user.created_at = datetime.utcnow()  # Записываем текущее время и дату
            await self.update_user(user)
        except TelegramUser.DoesNotExist:
            pass  # Если пользователь не найден, ничего не делаем

    async def receive(self, text_data):
        from mainapp.models import TelegramUser
        data = json.loads(text_data)
        increment = data.get('increment', 1)
        type = data.get('type','')


        print(f"Received increment: {increment} for user_id: {self.user_id}")  # Используем self.user_id здесь
        try:
            user = await self.get_user(TelegramUser, self.user_id)  # Используем self.user_id здесь
            if user:  # Проверка на существование пользователя
                print(f"User found: {user}")
                user.balance += increment
                print(f"New balance: {user.balance} for user_id: {self.user_id}")  # Используем self.user_id здесь
                await self.update_user(user)  # Асинхронная операция сохранения пользователя
                
                # Отправьте обновленный баланс обратно клиенту
                await self.send(text_data=json.dumps({
                    'balance': user.balance
                }))
            else:
                print(f"User with id {self.user_id} not found")  # Используем self.user_id здесь
        except TelegramUser.DoesNotExist:
            await self.send(text_data=json.dumps({
                'error': 'User does not exist'
            }))

    @database_sync_to_async
    def get_user(self, model, user_id):
        try:
            user = model.objects.get(user_id=user_id)
            return user
        except model.DoesNotExist:
            return None

    @database_sync_to_async
    def update_user(self, user):
        user.save()
        print(f"User {user.user_id} saved with new balance: {user.balance}")
