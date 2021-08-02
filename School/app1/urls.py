from django.urls import path
from .views import student_registration, student_login

urlpatterns = [
    path('student_registration', student_registration, name='student_registration'),
    path('student_login', student_login, name='student_login')
]
