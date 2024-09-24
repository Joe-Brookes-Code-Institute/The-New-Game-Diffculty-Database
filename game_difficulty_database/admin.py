from django.contrib import admin
from .models import Game
from .forms import GameForm

class GameAdmin(admin.ModelAdmin):
    form = GameForm
    list_display = ('name', 'default_difficulty', 'custom_difficulty_allowed', 'new_game_plus')
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            (None, {
                'fields': ('name', 'description', 'default_difficulty', 'custom_difficulty_allowed', 'new_game_plus')
            }),
        ]
        
        difficulty_fields = []
        for difficulty, display_name in Game.DIFFICULTY_CHOICES:
            difficulty_fields.extend([f'{difficulty}_player_health', f'{difficulty}_enemy_health'])
        
        fieldsets.append((
            'Difficulty Settings',
            {'fields': difficulty_fields, 'classes': ('collapse',)}
        ))
        
        return fieldsets

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:
            difficulty_settings = obj.difficulty_settings
            for difficulty, _ in Game.DIFFICULTY_CHOICES:
                for setting in ['player_health', 'enemy_health']:
                    field_name = f'{difficulty}_{setting}'
                    if field_name in form.base_fields:
                        form.base_fields[field_name].initial = difficulty_settings.get(difficulty, {}).get(setting, 100)
        return form

    def save_model(self, request, obj, form, change):
        difficulty_settings = {}
        for difficulty, _ in Game.DIFFICULTY_CHOICES:
            difficulty_settings[difficulty] = {}
            for setting in ['player_health', 'enemy_health']:
                field_name = f'{difficulty}_{setting}'
                value = form.cleaned_data.get(field_name)
                if value is not None:
                    difficulty_settings[difficulty][setting] = value
        obj.difficulty_settings = difficulty_settings
        super().save_model(request, obj, form, change)

admin.site.register(Game, GameAdmin)