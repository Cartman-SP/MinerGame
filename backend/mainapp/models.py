from django.db import models

class TelegramUser(models.Model):
    user_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=128)
    usertag = models.CharField(max_length=128)
    balance = models.IntegerField(default=5000)
    gpc = models.IntegerField(default=2)
    lvl = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Room(models.Model):
    lvl  = models.IntegerField()
    comp_lvl = models.IntegerField(default=1)
    webcam_lvl = models.IntegerField(default=1)
    micro_lvl = models.IntegerField(default=1)
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    