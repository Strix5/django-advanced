from django.urls import path

from . import views

app_name = 'htmx'


urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('add_game/', views.add_game, name='add_game')
]
