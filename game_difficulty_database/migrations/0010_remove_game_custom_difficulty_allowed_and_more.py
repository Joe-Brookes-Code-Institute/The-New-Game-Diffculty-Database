# Generated by Django 4.2.16 on 2024-09-24 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_difficulty_database', '0009_game_difficulty_settings_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='custom_difficulty_allowed',
        ),
        migrations.RemoveField(
            model_name='game',
            name='difficulty_settings',
        ),
        migrations.RemoveField(
            model_name='game',
            name='new_game_plus',
        ),
        migrations.AlterField(
            model_name='difficultysettings',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='difficulty_settings', to='game_difficulty_database.game'),
        ),
    ]
