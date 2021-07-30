from django.urls import path
from . import views

urlpatterns = [
    path('',views.sign_up,name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change/',views.user_change_pass, name='change')
]
