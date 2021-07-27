from django.urls import path
from .views import show, udata, ddata

urlpatterns = [
    path("", show),
    path("udata", udata,name = 'udata'),
    path("ddata", ddata,name = 'ddata'),
]
