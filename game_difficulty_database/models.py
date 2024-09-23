from django.db import models

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
    
    name = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='normal')
    description = models.TextField(blank=True)  # Made optional

    # New fields for difficulty settings, made optional
    enemy_health = models.IntegerField(null=True, blank=True, help_text="Enemy health percentage")
    player_health = models.IntegerField(null=True, blank=True, help_text="Player health percentage")
    resources = models.IntegerField(null=True, blank=True, help_text="Resources percentage")

    # Checkboxes, made optional
    unlockable = models.BooleanField(default=False, blank=True)
    new_game_plus = models.BooleanField(default=False, blank=True)
    Custom_Difficulty = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name