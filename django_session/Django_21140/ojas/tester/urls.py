from django.urls import path
from . import views
urlpatterns = [
    path('greeting', views.greeting, name='HomePage'),
    path('bye', views.bye, name='ByePage')
]
