from django.urls import path
from .views import show, udata, ddata

urlpatterns = [
    path("show", show, name = 'show'),
    path("udata/<int:id>/", udata,name = 'udata'),
    path("ddata/<int:id>/", ddata,name = 'ddata'),
]
