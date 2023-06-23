from django.shortcuts import render, redirect

from GamesPlayApp.game.forms import GameForm, DeleteGame
from GamesPlayApp.game.models import Game


# Create your views here.

def create_game(request):
    form = GameForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {'form': form}
    return render(request, template_name='game/create-game.html', context=context)


def game_details(request, game_id):
    game = Game.objects.get(id=game_id)
    context = {'game': game}
    return render(request, template_name='game/details-game.html', context=context)


def edit_game(request, game_id):
    game = Game.objects.get(id=game_id)

    if request.method == 'GET':
        context = {'form': GameForm(initial=game.__dict__)}
        return render(request, template_name='game/edit-game.html', context=context)

    else:
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

        else:
            context = {'form': form}
            return render(request, template_name='game/edit-game.html', context=context)


def delete_game(request, game_id):
    game = Game.objects.get(id=game_id)

    if request.method == 'GET':
        context = {'form': DeleteGame(initial=game.__dict__)}
        return render(request, template_name='game/delete-game.html', context=context)

    else:
        form = DeleteGame(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

        else:
            context = {'form': form}
            return render(request, template_name='game/delete-game.html', context=context)

