from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods

from .models import Game
from .forms import GameAddForm, GameEditForm


@require_http_methods(['GET'])
def game_list(request):
    list_game = Game.objects.all()
    form = GameAddForm(auto_id=False)
    return render(request, 'base.html', {'game_list': list_game,
                                         'form': form})


@require_http_methods(['POST'])
def add_game(request):
    form = GameAddForm(request.POST)
    if form.is_valid():
        game = form.save()
    return render(request, 'htmx/partial_game_detail.html', {'game': game})


@require_http_methods(['GET'])
def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'htmx/partial_game_detail.html', context=
                  {'game': game})


def game_edit(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            game = form.save()
            return render(request, 'htmx/partial_game_detail.html', context={'game': game})
    else:
        form = GameEditForm(instance=game)
    return render(request, 'htmx/partial_game_update_form.html', context={'form': form, 'game': game})


@require_http_methods(['DELETE'])
def game_delete(request, pk):
    game = Game.objects.get(pk=pk)
    game.delete()
    return HttpResponse()


@require_http_methods(['PATCH'])
def game_played_status(request, pk):
    game = Game.objects.get(pk=pk)
    game.played = not game.played
    game.save()
    return render(request, 'htmx/partial_game_detail.html', {'game': game})


@require_http_methods(['GET'])
def game_list_sort(request, filter_field, direction):
    filter_field = '-' + filter_field if direction == 'descend' else filter_field
    list_game = Game.objects.order_by(filter_field)
    return render(request, 'htmx/partial_game_list.html', context={'game_list': list_game})
