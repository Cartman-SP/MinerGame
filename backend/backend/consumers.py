import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.apps import apps
from django.utils import timezone

class MiningConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_id = data['user_id']
        gph = data['gph']

        telegram_user = await self.get_or_create_telegram_user(user_id)
        if telegram_user:
            increment = gph / 3600 * telegram_user.modifier
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
        telegram_user.last_login = timezone.now()
        telegram_user.save()



class TapConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_id = data['user_id']
        increment = data['increment']
        taps = data['taps']

        telegram_user = await self.get_or_create_telegram_user(user_id)
        if telegram_user:
            if(telegram_user.energy > 0):
                telegram_user.balance += increment*taps
                telegram_user.energy -= taps
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




class EnergyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

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
        if telegram_user.max_energy < telegram_user.energy + 3:
            telegram_user.energy = telegram_user.max_energy
        else:
            telegram_user.energy += 3
        telegram_user.secs_in_game += 6
        telegram_user.last_login = timezone.now()
        telegram_user.save()
        return telegram_user.energy

    @database_sync_to_async
    def get_telegram_user(self, user_id):
        TelegramUser = apps.get_model('mainapp', 'TelegramUser')
        try:
            return TelegramUser.objects.get(user_id=user_id)
        except TelegramUser.DoesNotExist:
            return None
