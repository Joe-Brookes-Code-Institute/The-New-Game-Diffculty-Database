from django.contrib import admin
from .models import Game, DifficultySettings

class DifficultySettingsInline(admin.TabularInline):
    model = DifficultySettings
    extra = 1

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'recommended_difficulty')
    inlines = [DifficultySettingsInline]

class DifficultySettingsAdmin(admin.ModelAdmin):
    list_display = ('game', 'difficulty', 'player_health', 'enemy_health')
    list_filter = ('game', 'difficulty')

admin.site.register(Game, GameAdmin)
admin.site.register(DifficultySettings, DifficultySettingsAdmin)