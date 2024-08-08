from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib import admin

class TelegramUser(models.Model):
    user_id = models.CharField(max_length=254,unique=True)
    username = models.CharField(max_length=128)
    usertag = models.CharField(max_length=128)
    balance = models.FloatField(default=5000)
    lvl = models.IntegerField(default=1)
    energy = models.IntegerField(default=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    gph = models.FloatField(default=731)
    gpc = models.IntegerField(default=1)
    mining_end = models.DateTimeField(auto_now_add=True)
    mining_duration = models.DurationField(default=timedelta(minutes=60))
    mining_time_lvl = models.IntegerField(default=1)
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
    friends_invited = models.IntegerField(default=0)
    daily_reward_claimed = models.BooleanField(default=False)
    daily_reward_day = models.IntegerField(default=0)
    daily_reward_date = models.DateField(auto_now_add=True)
    secs_in_game = models.IntegerField(default=0)
    def update_mining_end(self):
        self.mining_end = timezone.now() + self.mining_duration
        self.save()
    def __str__(self):
        return self.usertag
class Referal(models.Model):
    inviter = models.ForeignKey(TelegramUser, related_name='invitations', on_delete=models.CASCADE)
    user = models.ForeignKey(TelegramUser, related_name='referrals', on_delete=models.CASCADE)


class Room(models.Model):
    lvl  = models.IntegerField()
    comp_lvl = models.IntegerField(default=1)
    webcam_lvl = models.IntegerField(default=1)
    micro_lvl = models.IntegerField(default=1)
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    
class Task(models.Model):
    reward = models.IntegerField()
    typeT = models.CharField(max_length=128)
    channel_id = models.CharField(max_length=254)
    site_link = models.CharField(max_length=254)
    friends_toAdd = models.IntegerField()

class UserTask(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    friends_invited = models.IntegerField(default=0)


admin.site.register(TelegramUser)

