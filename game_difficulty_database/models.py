from django.db import models

class Game(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    name = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    genre = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    release_date = models.DateField()
    NGplus = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.name