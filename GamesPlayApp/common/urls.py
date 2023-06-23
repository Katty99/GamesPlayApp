from django.urls import path, include

from GamesPlayApp.common import views

urlpatterns = [
    path('', views.home, name='home')
]