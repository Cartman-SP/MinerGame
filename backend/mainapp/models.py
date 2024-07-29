from django.db import models
from django.utils import timezone
from datetime import timedelta

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
    def update_mining_end(self):
        self.mining_end = timezone.now() + self.mining_duration
        self.save()

class Room(models.Model):
    lvl  = models.IntegerField()
    comp_lvl = models.IntegerField(default=1)
    webcam_lvl = models.IntegerField(default=1)
    micro_lvl = models.IntegerField(default=1)
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    