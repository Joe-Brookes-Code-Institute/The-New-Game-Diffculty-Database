from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'difficulty', 'release_date', 'description', 
                  'enemy_health', 'player_health', 'resources', 
                  'unlockable', 'new_game_plus']