# Generated by Django 4.2 on 2023-04-24 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tttwars', '0007_tttwarsgame_delete_gamerequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tttwarsgame',
            name='game_id',
        ),
    ]