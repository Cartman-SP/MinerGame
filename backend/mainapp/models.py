from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib import admin

class TelegramUser(models.Model):
    user_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=128)
    usertag = models.CharField(max_length=128)
    balance = models.FloatField(default=5000)
    lvl = models.IntegerField(default=1)
    energy = models.IntegerField(default=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    gph = models.FloatField(default=6.25)
    gpc = models.IntegerField(default=1)
    mining_end = models.DateTimeField(auto_now_add=True)
    mining_duration = models.DurationField(default=timedelta(minutes=30))
    last_login = models.DateTimeField(null=True, blank=True)
    max_energy = models.IntegerField(default=2000)
    enery_lvl = models.IntegerField(default=1)
    tap_lvl = models.IntegerField(default=1)
    refresh_energy = models.IntegerField(default=5)
    refresh_energy_date = models.DateField(auto_now_add=True)
    video_lvl = models.IntegerField(default=1)
    modifier = models.FloatField(default=1)
    subscribed = models.BooleanField(default=False)
    subscribe_money_gived = models.BooleanField(default=False)
    photo_url = models.URLField(blank=True, null=True)
    ispremium = models.BooleanField(default=False)
    def update_mining_end(self):
        self.mining_end = timezone.now() + self.mining_duration
        self.save()

class Referal(models.Model):
    inviter = models.ForeignKey(TelegramUser, related_name='invitations', on_delete=models.CASCADE)
    user = models.ForeignKey(TelegramUser, related_name='referrals', on_delete=models.CASCADE)


class Room(models.Model):
    lvl  = models.IntegerField()
    comp_lvl = models.IntegerField(default=1)
    webcam_lvl = models.IntegerField(default=1)
    micro_lvl = models.IntegerField(default=1)
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    
admin.register(TelegramUser)