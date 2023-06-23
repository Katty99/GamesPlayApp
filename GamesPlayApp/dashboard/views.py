from django.shortcuts import render

from GamesPlayApp.game.models import Game


# Create your views here.
def dashboard(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, template_name='templates/dashboard.html', context=context)
