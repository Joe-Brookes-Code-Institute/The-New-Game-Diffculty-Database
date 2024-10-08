# Generated by Django 4.2.16 on 2024-09-24 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_difficulty_database', '0008_remove_game_difficulty_settings_difficultysettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='difficulty_settings',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='difficultysettings',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='difficulty_settings_list', to='game_difficulty_database.game'),
        ),
    ]
