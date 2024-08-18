from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

app_name = 'htmx'


urlpatterns = [
    path('', views.game_list, name='game_list'),
    path(_('add_game/'), views.add_game, name='add_game'),
    path(_('game_detail/<int:pk>/'), views.game_detail, name='game_detail'),
    path(_('game_edit/<int:pk>/'), views.game_edit, name='game_edit'),
    path(_('game_delete/<int:pk>/'), views.game_delete, name='game_delete'),
    path(_('game_played_status/<int:pk>/'), views.game_played_status, name='game_played_status'),
    path(_('game_list_sort/<str:filter_field>/<str:direction>/'), views.game_list_sort, name='game_list_sort'),
]
