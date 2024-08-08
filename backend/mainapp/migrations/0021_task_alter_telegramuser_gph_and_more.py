# Generated by Django 5.0.6 on 2024-08-08 01:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_telegramuser_secs_in_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward', models.IntegerField()),
                ('typeT', models.CharField(max_length=128)),
                ('channel_id', models.CharField(max_length=256)),
                ('group_link', models.CharField(max_length=256)),
                ('friends_toAdd', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='gph',
            field=models.FloatField(default=731),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='user_id',
            field=models.CharField(max_length=1000, unique=True),
        ),
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete', models.BooleanField(default=False)),
                ('friends_invited', models.IntegerField(default=0)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.telegramuser')),
            ],
        ),
    ]
