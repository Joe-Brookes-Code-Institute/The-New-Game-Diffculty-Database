# Generated by Django 4.2.16 on 2024-09-24 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_difficulty_database', '0007_alter_game_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='difficulty_settings',
        ),
        migrations.CreateModel(
            name='DifficultySettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(choices=[('extremely_easy', 'Extremely Easy'), ('very_easy', 'Very Easy'), ('easy', 'Easy'), ('somewhat_easy', 'Somewhat Easy'), ('normal', 'Normal'), ('somewhat_hard', 'Somewhat Hard'), ('hard', 'Hard'), ('very_hard', 'Very Hard'), ('extremely_hard', 'Extremely Hard')], max_length=20)),
                ('player_health', models.IntegerField(default=100)),
                ('enemy_health', models.IntegerField(default=100)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='difficulty_settings', to='game_difficulty_database.game')),
            ],
            options={
                'unique_together': {('game', 'difficulty')},
            },
        ),
    ]
