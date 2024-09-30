from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Game, DifficultySettings, UserProfile, UserGamePreference
from .forms import GameForm, GameDifficultySettingsFormSet, UserProfileForm, UserGamePreferenceForm

def game_list(request):
    games = Game.objects.all().order_by('name')
    introduction_text = "Welcome to the official blog of the Game Difficulty Database, your ultimate resource for finding games that match your skill level. Whether you're a casual player looking for a relaxing experience or a hardcore gamer seeking the next big challenge, our database has something for everyone."
    
    return render(request, 'game_difficulty_database/game_list.html', {
        'games': games,
        'introduction_text': introduction_text,
    })

def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    difficulty_settings = game.difficulty_settings.all()
    user_preference = None
    if request.user.is_authenticated:
        user_preference, created = UserGamePreference.objects.get_or_create(user=request.user, game=game)
    return render(request, 'game_difficulty_database/game_detail.html', {
        'game': game, 
        'difficulty_settings': difficulty_settings,
        'user_preference': user_preference,
    })

@login_required
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        formset = GameDifficultySettingsFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            game = form.save(commit=False)
            game.added_by = request.user
            game.save()
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

@login_required
def update_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)
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

@login_required
def delete_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        game_name = game.name
        game.delete()
        messages.success(request, f"Game '{game_name}' was successfully deleted.")
        return redirect('game_list')
    return render(request, 'game_difficulty_database/delete_game.html', {'game': game})

@login_required
def profile_view(request):
    profile = request.user.userprofile
    return render(request, 'game_difficulty_database/profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile was successfully updated!")
            return redirect('profile_view')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'game_difficulty_database/edit_profile.html', {'form': form})

@login_required
def set_game_preference(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    preference, created = UserGamePreference.objects.get_or_create(user=request.user, game=game)
    if request.method == 'POST':
        form = UserGamePreferenceForm(request.POST, instance=preference)
        if form.is_valid():
            form.save()
            messages.success(request, f"Preference for '{game.name}' updated successfully!")
            return redirect('game_detail', game_id=game.id)
    else:
        form = UserGamePreferenceForm(instance=preference)
    return render(request, 'game_difficulty_database/set_game_preference.html', {'form': form, 'game': game})   
    
def game_list(request):
    games = Game.objects.all().order_by('name')  # Replace 'name' with the field you want to sort by
    return render(request, 'game_difficulty_database/game_list.html', {'games': games})