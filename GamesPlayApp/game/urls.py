from django.urls import path, include

from GamesPlayApp.game import views

urlpatterns = [
    path('create/', views.create_game, name='create_game'),
    path('details/<int:game_id>/', views.game_details, name='game_details'),
    path('edit/<int:game_id>/', views.edit_game, name='edit_game'),
    path('delete/<int:game_id>/', views.delete_game, name='delete_game'),
]
