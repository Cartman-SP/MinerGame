# Generated by Django 5.0.6 on 2024-07-28 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_telegramuser_mining_duration_telegramuser_mining_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='balance',
            field=models.FloatField(default=5000),
        ),
    ]
