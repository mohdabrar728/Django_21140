from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('f/', views.showcase),
    path('s/', views.showcase1),
    path('t/', views.showcase2),
]
