from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

from .models import Game
from .forms import GameAddForm


@require_http_methods(['GET'])
def game_list(request):
    list_game = Game.objects.all()
    form = GameAddForm(auto_id=False)
    return render(request, 'base.html', {'game_list': list_game,
                                         'form': form})


# @require_http_methods(['POST'])
def add_game(request):
    form = GameAddForm(request.POST)
    if form.is_valid():
        game = form.save()
    return render(request, 'htmx/partial_game_detail.html', {'game': game})
