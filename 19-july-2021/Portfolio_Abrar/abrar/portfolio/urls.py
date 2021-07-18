from django.urls import path
from . import views
urlpatterns = [
    path("",views.home),
    path("home",views.home),
    path("about", views.about),
    path("resume", views.resume),
    path("project", views.project),
    path("research_paper", views.research_paper),
    path("contact", views.contact),
]