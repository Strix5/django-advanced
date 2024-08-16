from django.urls import path

from . import views

app_name = 'htmx'


urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('add_game/', views.add_game, name='add_game'),
    path('game_detail/<int:pk>/', views.game_detail, name='game_detail'),
    path('game_edit/<int:pk>/', views.game_edit, name='game_edit'),
    path('game_delete/<int:pk>/', views.game_delete, name='game_delete'),
    path('game_played_status/<int:pk>/', views.game_played_status, name='game_played_status'),
    path('game_list_sort/<str:filter_field>/<str:direction>/', views.game_list_sort, name='game_list_sort'),
]
