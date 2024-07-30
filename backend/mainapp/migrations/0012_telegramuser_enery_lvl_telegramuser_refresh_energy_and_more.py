# Generated by Django 5.0.6 on 2024-07-30 15:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_telegramuser_max_energy'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='enery_lvl',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='refresh_energy',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='refresh_energy_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='tap_lvl',
            field=models.IntegerField(default=1),
        ),
    ]
