from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('add/', views.add_game, name='add_game'),  # Add this line if it's missing
]
    # Add other paths as needed
