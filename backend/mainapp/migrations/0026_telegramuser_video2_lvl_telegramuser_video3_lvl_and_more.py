# Generated by Django 5.0.6 on 2024-08-11 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0025_telegramuser_wallet_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='video2_lvl',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='video3_lvl',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='video4_lvl',
            field=models.IntegerField(default=0),
        ),
    ]
