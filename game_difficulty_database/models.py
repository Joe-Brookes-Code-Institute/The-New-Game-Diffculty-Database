from django.db import models
from django.core.exceptions import ValidationError

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
    difficulty_settings = models.JSONField(default=dict)
    custom_difficulty_allowed = models.BooleanField(default=False)
    new_game_plus = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def clean(self):
        if not isinstance(self.difficulty_settings, dict):
            raise ValidationError("Difficulty settings must be a dictionary")
        for difficulty, settings in self.difficulty_settings.items():
            if difficulty not in dict(self.DIFFICULTY_CHOICES):
                raise ValidationError(f"Invalid difficulty level: {difficulty}")
            if not isinstance(settings, dict):
                raise ValidationError(f"Settings for {difficulty} must be a dictionary")
            for setting, value in settings.items():
                if setting not in ['player_health', 'enemy_health']:
                    raise ValidationError(f"Invalid setting for {difficulty}: {setting}")
                if not isinstance(value, int) or value < 0 or value > 200:
                    raise ValidationError(f"Invalid value for {difficulty} {setting}: {value}")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)