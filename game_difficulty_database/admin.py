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
        for difficulty, _ in Game.DIFFICULTY_CHOICES:
            for setting in ['player_health', 'enemy_health', 'resources', 'enemy_damage']:
                difficulty_fields.append(f'{difficulty}_{setting}')
        
        fieldsets.append(('Difficulty Settings', {'fields': difficulty_fields, 'classes': ('collapse',)}))
        
        return fieldsets

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:
            for difficulty, _ in Game.DIFFICULTY_CHOICES:
                for setting in ['player_health', 'enemy_health', 'resources', 'enemy_damage']:
                    field_name = f'{difficulty}_{setting}'
                    if field_name in form.base_fields:
                        form.base_fields[field_name].initial = obj.difficulty_settings.get(difficulty, {}).get(setting, 100)
        return form

admin.site.register(Game, GameAdmin)