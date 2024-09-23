from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'description', 'default_difficulty', 'custom_difficulty_allowed', 'new_game_plus']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for difficulty, _ in Game.DIFFICULTY_CHOICES:
            for setting in ['player_health', 'enemy_health', 'resources', 'enemy_damage']:
                field_name = f'{difficulty}_{setting}'
                self.fields[field_name] = forms.IntegerField(
                    required=False,
                    min_value=0,
                    max_value=200,
                    initial=100,
                    label=f'{difficulty.replace("_", " ").title()} {setting.replace("_", " ").title()}'
                )

    def clean(self):
        cleaned_data = super().clean()
        difficulty_settings = {}
        for difficulty, _ in Game.DIFFICULTY_CHOICES:
            difficulty_settings[difficulty] = {}
            for setting in ['player_health', 'enemy_health', 'resources', 'enemy_damage']:
                field_name = f'{difficulty}_{setting}'
                value = cleaned_data.get(field_name)
                if value is not None:
                    difficulty_settings[difficulty][setting] = value
        cleaned_data['difficulty_settings'] = difficulty_settings
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.difficulty_settings = self.cleaned_data['difficulty_settings']
        if commit:
            instance.save()
        return instance