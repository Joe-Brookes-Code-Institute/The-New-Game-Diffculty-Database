from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('add/', views.add_game, name='add_game'),
    # Add other paths as needed
]