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
    release_date = models.DateField()
    description = models.TextField()

    # New fields for difficulty settings
    enemy_health = models.IntegerField(default=100, help_text="Enemy health percentage")
    player_health = models.IntegerField(default=100, help_text="Player health percentage")
    resources = models.IntegerField(default=100, help_text="Resources percentage")

    # Checkboxes
    unlockable = models.BooleanField(default=False)
    new_game_plus = models.BooleanField(default=False)

    def __str__(self):
        return self.name