from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Game(models.Model):
    DIFFICULTY_CHOICES = [
        ('extremely_easy', 'Extremely Easy'),
        ('very_easy', 'Very Easy'),
        ('easy', 'Easy'),
        ('somewhat_easy', 'Somewhat Easy'),
        ('normal', 'Normal'),
        ('somewhat_hard', 'Somewhat Hard'),
        ('hard', 'Hard'),
        ('very_hard', 'Very Hard'),
        ('extremely_hard', 'Extremely Hard'),
    ]
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    default_difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='normal')
    image = models.ImageField(upload_to='game_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class DifficultySettings(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='difficulty_settings')
    difficulty = models.CharField(max_length=20, choices=Game.DIFFICULTY_CHOICES)
    player_health = models.IntegerField(default=100, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    enemy_health = models.IntegerField(default=100, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    unlockable = models.BooleanField(default=False)

    class Meta:
        unique_together = ['game', 'difficulty']

    def __str__(self):
        return f"{self.game.name} - {self.get_difficulty_display()}"