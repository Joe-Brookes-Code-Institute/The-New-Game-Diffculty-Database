from django.shortcuts import render, get_object_or_404, redirect
from .models import Game
from .forms import GameForm  # Make sure you have this import

def game_list(request):
    games = Game.objects.all().order_by('name')
    return render(request, 'game_difficulty_database/game_list.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    selected_difficulty = request.GET.get('difficulty', game.default_difficulty)
    
    difficulty_data = game.difficulty_settings.get(selected_difficulty, {})
    
    context = {
        'game': game,
        'difficulties': Game.DIFFICULTY_CHOICES,
        'selected_difficulty': selected_difficulty,
        'difficulty_data': difficulty_data,
    }
    return render(request, 'game_difficulty_database/game_detail.html', context)

# Add this new view function
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm()
    return render(request, 'game_difficulty_database/add_game.html', {'form': form})