from django.shortcuts import render, redirect

from GamesPlayApp.account.forms import ProfileForm, EditProfile
from GamesPlayApp.account.models import Profile
from GamesPlayApp.game.models import Game


# Create your views here.
def create_profile(request):
    form = ProfileForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, template_name='account/create-profile.html', context=context)


def profile_details(request):
    profile = Profile.objects.first()
    games = Game.objects.all()
    total_games = len(games)
    total_rating = 0
    for game in games:
        total_rating += game.rate

    if total_games:
        average_rating = total_rating / total_games
    else:
        average_rating = 0
    context = {'profile': profile, 'total_games': total_games, 'average_rating': average_rating}
    return render(request, template_name='account/details-profile.html', context=context)


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        context = {'form': EditProfile(initial=profile.__dict__)}
        return render(request, template_name='account/edit-profile.html', context=context)

    else:
        form = EditProfile(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
        else:
            context = {'form': form}
            return render(request, template_name='account/edit-profile.html', context=context)


def delete_profile(request):
    profile = Profile.objects.first()
    games = Game.objects.all()
    if request.method == "POST":
        profile.delete()
        games.delete()
        return redirect('home')
    return render(request, template_name='account/delete-profile.html')
