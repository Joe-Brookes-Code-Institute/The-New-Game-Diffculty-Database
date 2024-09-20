from django.shortcuts import render
from .models import Game

def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_difficulty_database/game_list.html', {'games': games})

def add_game(request):
    # This is a placeholder. You'll implement the actual logic later.
    return render(request, 'game_difficulty_database/add_game.html')