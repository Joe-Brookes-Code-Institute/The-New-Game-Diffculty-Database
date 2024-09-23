from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'difficulty', 'description', 
                  'enemy_health', 'player_health', 'resources', 
                  'unlockable', 'new_game_plus', 'Custom_Difficulty']

    def __init__(self, *args, **kwargs):
        super(GameForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ['name', 'difficulty']:
                self.fields[field].required = False