# Generated by Django 4.2 on 2023-04-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tttwars', '0019_rename_dgame1score_tttwarsgame_p1game1score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tttwarsgame',
            name='p1rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='p2rating',
            field=models.IntegerField(default=0),
        ),
    ]
