import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.apps import apps
from django.utils import timezone

class MiningConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.mining_task = asyncio.create_task(self.mine_resources())

    async def disconnect(self, close_code):
        if hasattr(self, 'mining_task') and self.mining_task:
            self.mining_task.cancel()
        await self.update_last_login()

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_id = data['user_id']
        gph = data['gph']

        telegram_user = await self.get_or_create_telegram_user(user_id)
        if telegram_user:
            increment = gph / 720
            telegram_user.balance += increment
            await self.update_telegram_user(telegram_user)

            await self.send(text_data=json.dumps({
                'balance': telegram_user.balance,
                'energy': telegram_user.energy,
            }))

    async def mine_resources(self):
        while True:
            await asyncio.sleep(5)
            await self.send_mining_data()

    async def send_mining_data(self):
        user_id = self.scope["user"].id
        telegram_user = await self.get_or_create_telegram_user(user_id)
        if telegram_user:
            increment = telegram_user.gph / 720
            telegram_user.balance += increment
            await self.update_telegram_user(telegram_user)

            await self.send(text_data=json.dumps({
                'balance': telegram_user.balance,
                'energy': telegram_user.energy,
            }))

    @database_sync_to_async
    def get_or_create_telegram_user(self, user_id):
        TelegramUser = apps.get_model('mainapp', 'TelegramUser')
        telegram_user, created = TelegramUser.objects.get_or_create(user_id=user_id)
        return telegram_user

    @database_sync_to_async
    def update_telegram_user(self, telegram_user):
        telegram_user.save()

    @database_sync_to_async
    def update_last_login(self):
        user_id = self.scope["user"].id
        TelegramUser = apps.get_model('mainapp', 'TelegramUser')
        telegram_user = TelegramUser.objects.get(user_id=user_id)
        telegram_user.last_login = timezone.now()
        telegram_user.save()

class TapConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        await self.update_last_login()

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_id = data['user_id']
        increment = data['increment']

        telegram_user = await self.get_or_create_telegram_user(user_id)
        if telegram_user:
            telegram_user.balance += increment
            telegram_user.energy -= 1
            await self.update_telegram_user(telegram_user)

            await self.send(text_data=json.dumps({
                'balance': telegram_user.balance,
                'energy': telegram_user.energy,
            }))

    @database_sync_to_async
    def get_or_create_telegram_user(self, user_id):
        TelegramUser = apps.get_model('mainapp', 'TelegramUser')
        telegram_user, created = TelegramUser.objects.get_or_create(user_id=user_id)
        return telegram_user

    @database_sync_to_async
    def update_telegram_user(self, telegram_user):
        telegram_user.save()

    @database_sync_to_async
    def update_last_login(self):
        user_id = self.scope["user"].id
        TelegramUser = apps.get_model('mainapp', 'TelegramUser')
        try:
            telegram_user = TelegramUser.objects.get(user_id=user_id)
            telegram_user.last_login = timezone.now()
            telegram_user.save()
        except TelegramUser.DoesNotExist:
            print(f"TelegramUser with user_id {user_id} does not exist.")


class EnergyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        await self.update_last_login()

    async def receive(self, text_data):
        user_id = json.loads(text_data).get('user_id')
        telegram_user = await self.get_telegram_user(user_id)
        if telegram_user:
            energy = await self.increase_energy(telegram_user)
            await self.send(text_data=json.dumps({
                'energy': energy,
            }))

    @database_sync_to_async
    def increase_energy(self, telegram_user):
        if telegram_user.max_energy < telegram_user.energy + 5:
            telegram_user.energy = telegram_user.max_energy
        else:
            telegram_user.energy += 5
        telegram_user.save()
        return telegram_user.energy

    @database_sync_to_async
    def get_telegram_user(self, user_id):
        TelegramUser = apps.get_model('mainapp', 'TelegramUser')
        try:
            return TelegramUser.objects.get(user_id=user_id)
        except TelegramUser.DoesNotExist:
            return None

    @database_sync_to_async
    def update_last_login(self):
        user_id = self.scope["user"].id
        TelegramUser = apps.get_model('mainapp', 'TelegramUser')
        try:
            telegram_user = TelegramUser.objects.get(user_id=user_id)
            telegram_user.last_login = timezone.now()
            telegram_user.save()
        except TelegramUser.DoesNotExist:
            print(f"TelegramUser with user_id {user_id} does not exist.")
