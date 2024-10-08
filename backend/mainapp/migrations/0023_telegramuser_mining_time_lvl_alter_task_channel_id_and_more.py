# Generated by Django 5.0.6 on 2024-08-08 19:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_rename_group_link_task_site_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='mining_time_lvl',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='channel_id',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='task',
            name='site_link',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='mining_duration',
            field=models.DurationField(default=datetime.timedelta(seconds=3600)),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='user_id',
            field=models.CharField(max_length=254, unique=True),
        ),
    ]
