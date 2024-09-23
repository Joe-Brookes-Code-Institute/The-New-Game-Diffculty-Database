from django.shortcuts import render, get_object_or_404
from .models import Game

def game_list(request):
    games = Game.objects.all().order_by('name')
    return render(request, 'game_difficulty_database/game_list.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game_difficulty_database/game_detail.html', {'game': game})
