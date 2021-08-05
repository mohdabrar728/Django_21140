from django.urls import path
from . import views

urlpatterns = [
    path('', views.fun_home),
    path('home', views.fun_home),
    path('blogs', views.fun_blog),
    path('cricket', views.fun_cricket),
    path('football', views.fun_football),
    path('players', views.fun_players)
]