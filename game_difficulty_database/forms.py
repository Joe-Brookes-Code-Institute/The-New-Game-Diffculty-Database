from django import forms
from .models import Game, DifficultySettings, UserProfile, UserGamePreference

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'favorite_game', 'preferred_difficulty', 'avatar']

class UserGamePreferenceForm(forms.ModelForm):
    class Meta:
        model = UserGamePreference
        fields = ['game', 'preferred_difficulty']

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