# Generated by Django 4.2.16 on 2024-09-23 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_difficulty_database', '0006_rename_difficulty_game_default_difficulty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]