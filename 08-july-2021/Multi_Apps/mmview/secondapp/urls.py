from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('i/', views.saview),
    path('f/', views.saview1),
    path('s/', views.saview2),
]
