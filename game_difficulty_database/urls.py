from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('<int:game_id>/', views.game_detail, name='game_detail'),
    path('add/', views.add_game, name='add_game'),
    path('<int:game_id>/update/', views.update_game, name='update_game'),
    path('<int:game_id>/delete/', views.delete_game, name='delete_game'),
]