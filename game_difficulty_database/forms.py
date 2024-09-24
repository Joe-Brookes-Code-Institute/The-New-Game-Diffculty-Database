from django import forms
from .models import Game, DifficultySettings

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'description', 'default_difficulty', 'image']

class DifficultySettingsForm(forms.ModelForm):
    class Meta:
        model = DifficultySettings
        fields = ['difficulty', 'player_health', 'enemy_health', 'unlockable']

GameDifficultySettingsFormSet = forms.inlineformset_factory(
    Game, DifficultySettings, form=DifficultySettingsForm,
    extra=len(Game.DIFFICULTY_CHOICES), max_num=len(Game.DIFFICULTY_CHOICES),
    can_delete=False
)