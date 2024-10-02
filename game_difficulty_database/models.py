from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    recommended_difficulty = models.CharField(
        max_length=50, 
        choices=DIFFICULTY_CHOICES, 
        default='normal'
    ) 
    image = CloudinaryField('image', null=True, blank=True)
    added_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.name

class DifficultySettings(models.Model):
    game = models.ForeignKey(
        Game, 
        on_delete=models.CASCADE, 
        related_name='difficulty_settings'
    )
    difficulty = models.CharField(max_length=20, choices=Game.DIFFICULTY_CHOICES)
    player_health = models.IntegerField(
        default=100, 
        validators=[MinValueValidator(1), MaxValueValidator(1000)]
    )
    enemy_health = models.IntegerField(
        default=100, 
        validators=[MinValueValidator(1), MaxValueValidator(1000)]
    )
    unlockable = models.BooleanField(default=False)

    class Meta:
        unique_together = ['game', 'difficulty']

    def __str__(self):
        return f"{self.game.name} - {self.get_difficulty_display()}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    favorite_game = models.ForeignKey(
        Game, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    preferred_difficulty = models.CharField(
        max_length=20, 
        choices=Game.DIFFICULTY_CHOICES, 
        default='normal'
    )
    avatar = CloudinaryField('avatar', null=True, blank=True)

    def __str__(self):
        return self.user.username

class UserGamePreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    preferred_difficulty = models.CharField(max_length=20, choices=Game.DIFFICULTY_CHOICES)

    class Meta:
        unique_together = ['user', 'game']

    def __str__(self):
        return f"{self.user.username}'s preference for {self.game.name}"

# Signal to create UserProfile automatically when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Signal to save UserProfile automatically when a User is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
