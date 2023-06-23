from django.shortcuts import render

from GamesPlayApp.account.models import Profile


# Create your views here.
def home(request):
    profile = Profile.objects.first()
    context = {'profile': profile}
    return render(request, template_name='common/home-page.html', context=context)
