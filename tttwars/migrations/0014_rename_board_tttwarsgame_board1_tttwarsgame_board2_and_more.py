# Generated by Django 4.2 on 2023-04-24 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tttwars', '0013_tttwarsgame_gamenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tttwarsgame',
            old_name='board',
            new_name='board1',
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='board2',
            field=models.JSONField(default=[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]),
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='board3',
            field=models.JSONField(default=[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]),
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='board4',
            field=models.JSONField(default=[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]),
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='board5',
            field=models.JSONField(default=[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]),
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='board6',
            field=models.JSONField(default=[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]),
        ),
    ]
