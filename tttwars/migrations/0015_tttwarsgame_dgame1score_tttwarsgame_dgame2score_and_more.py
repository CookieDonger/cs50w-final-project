# Generated by Django 4.2 on 2023-04-24 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tttwars', '0014_rename_board_tttwarsgame_board1_tttwarsgame_board2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tttwarsgame',
            name='dgame1score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='dgame2score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='dgame3score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='dgame4score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='dgame5score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='dgame6score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='ogame1score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='ogame2score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='ogame3score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='ogame4score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='ogame5score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tttwarsgame',
            name='ogame6score',
            field=models.IntegerField(default=0),
        ),
    ]
