from django.urls import path, include

from GamesPlayApp.dashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard')
]