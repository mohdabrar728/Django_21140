from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('first', views.firstview),
    path('second', views.secondview),
    path('third', views.thirdview),
]