from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Game, DifficultySettings
from .forms import GameForm, GameDifficultySettingsFormSet

def game_list(request):
    games = Game.objects.all().order_by('name')
    return render(request, 'game_difficulty_database/game_list.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    difficulty_settings = game.difficulty_settings.all()
    return render(request, 'game_difficulty_database/game_detail.html', {'game': game, 'difficulty_settings': difficulty_settings})

def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        formset = GameDifficultySettingsFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            game = form.save()
            formset.instance = game
            formset.save()
            messages.success(request, f"Game '{game.name}' was successfully added!")
            return redirect('game_list')
        else:
            messages.error(request, "There was an error with your submission. Please check the form and try again.")
    else:
        form = GameForm()
        formset = GameDifficultySettingsFormSet()
    
    return render(request, 'game_difficulty_database/add_game.html', {'form': form, 'formset': formset})

def update_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        formset = GameDifficultySettingsFormSet(request.POST, instance=game)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, f"Game '{game.name}' was successfully updated!")
            return redirect('game_detail', game_id=game.id)
        else:
            messages.error(request, "There was an error with your submission. Please check the form and try again.")
    else:
        form = GameForm(instance=game)
        formset = GameDifficultySettingsFormSet(instance=game)
    
    return render(request, 'game_difficulty_database/update_game.html', {'form': form, 'formset': formset, 'game': game})

def delete_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        game_name = game.name
        game.delete()
        messages.success(request, f"Game '{game_name}' was successfully deleted.")
        return redirect('game_list')
    return render(request, 'game_difficulty_database/delete_game.html', {'game': game})