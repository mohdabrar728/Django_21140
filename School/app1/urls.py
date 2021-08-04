from django.urls import path
from .views import student_registration, student_login, logout, view_attendance,student_dashboard,leave

urlpatterns = [
    path('', student_registration, name='student_registration'),
    path('student_registration', student_registration, name='student_registration'),
    path('student_login', student_login, name='student_login'),
    path('home', student_login, name='home'),
    path('logout', logout, name='logout'),
    path('view_attendance', view_attendance, name='view_attendance'),
    path('student_dashboard', student_dashboard, name='student_dashboard'),
    path('leave', leave, name='leave')
]
