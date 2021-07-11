from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('i/', views.faview),
    path('f/', views.faview1),
    path('s/', views.faview2),
]
