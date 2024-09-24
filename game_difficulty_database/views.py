from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Game
from .forms import GameForm

def game_list(request):
    games = Game.objects.all().order_by('name')
    return render(request, 'game_difficulty_database/game_list.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    selected_difficulty = request.GET.get('difficulty', game.default_difficulty)
    
    # Check if the selected difficulty is valid for this game
    if selected_difficulty not in dict(Game.DIFFICULTY_CHOICES):
        selected_difficulty = game.default_difficulty
        messages.warning(request, f"Invalid difficulty selected. Showing default difficulty: {game.get_default_difficulty_display()}")
    
    difficulty_data = game.difficulty_settings.get(selected_difficulty, {})
    
    context = {
        'game': game,
        'difficulties': Game.DIFFICULTY_CHOICES,
        'selected_difficulty': selected_difficulty,
        'difficulty_data': difficulty_data,
    }
    return render(request, 'game_difficulty_database/game_detail.html', context)

def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.difficulty_settings = form.cleaned_data['difficulty_settings']
            game.save()
            messages.success(request, f"Game '{game.name}' was successfully added!")
            return redirect('game_list')
        else:
            messages.error(request, "There was an error with your submission. Please check the form and try again.")
    else:
        form = GameForm()
    
    settings = ['player_health', 'enemy_health']
    return render(request, 'game_difficulty_database/add_game.html', {'form': form, 'settings': settings})

def update_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            game = form.save(commit=False)
            game.difficulty_settings = form.cleaned_data['difficulty_settings']
            game.save()
            messages.success(request, f"Game '{game.name}' was successfully updated!")
            return redirect('game_detail', game_id=game.id)
        else:
            messages.error(request, "There was an error with your submission. Please check the form and try again.")
    else:
        form = GameForm(instance=game)
    
    settings = ['player_health', 'enemy_health']
    return render(request, 'game_difficulty_database/update_game.html', {'form': form, 'settings': settings, 'game': game})

def delete_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        game_name = game.name
        game.delete()
        messages.success(request, f"Game '{game_name}' was successfully deleted.")
        return redirect('game_list')
    return render(request, 'game_difficulty_database/delete_game.html', {'game': game})