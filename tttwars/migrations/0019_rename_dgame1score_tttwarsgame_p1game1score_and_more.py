# Generated by Django 4.2 on 2023-04-25 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tttwars', '0018_rename_offense_tttwarsgame_p1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tttwarsgame',
            old_name='dgame1score',
            new_name='p1game1score',
        ),
        migrations.RenameField(
            model_name='tttwarsgame',
            old_name='dgame2score',
            new_name='p1game2score',
        ),
        migrations.RenameField(
            model_name='tttwarsgame',
            old_name='dgame3score',
            new_name='p1game3score',
        ),
        migrations.RenameField(
            model_name='tttwarsgame',
            old_name='dgame4score',
            new_name='p1game4score',
        ),
        migrations.RenameField(
            model_name='tttwarsgame',
            old_name='dgame5score',
            new_name='p1game5score',
        ),
        migrations.RenameField(
            model_name='tttwarsgame',
            old_name='dgame6score',
            new_name='p1game6score',
        ),
        migrations.RenameField(
            model_name='tttwarsgame',
            old_name='dscore',
            new_name='p2game1score',
        ),
        migrations.RenameField(
            model_name='tttwarsgame',
            old_name='ogame1score',
            new_name='p2game2score',
        ),
        migrations.RenameField(
            model_name='tttwarsgame',
            old_name='ogame2score',
            new_name='p2game3score',
        ),
        migrations.RenameField(
            model_name='tttwarsgame',
            old_name='ogame3score',
            new_name='p2game4score',
        ),
        migrations.RenameField(
            model_name='tttwarsgame',
            old_name='ogame4score',
            new_name='p2game5score',
        ),
        migrations.RenameField(
            model_name='tttwarsgame',
            old_name='ogame5score',
            new_name='p2game6score',
        ),
        migrations.RenameField(
            model_name='tttwarsgame',
            old_name='ogame6score',
            new_name='score1',
        ),
        migrations.RenameField(
            model_name='tttwarsgame',
            old_name='oscore',
            new_name='score2',
        ),
    ]