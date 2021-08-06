from django.contrib import admin
from django.urls import path
from . import views
# Create your views here.
urlpatterns = [path('',views.home)]