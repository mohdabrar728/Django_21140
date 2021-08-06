from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .our_forms import StudentForm
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
from .models import ViewAttendance
from .our_forms import LeaveForm
import socket

User = get_user_model()


# Create your views here.
def student_registration(request):
    form_var = StudentForm(request.POST)
    if form_var.is_valid():
        form_var.save()
        form_var = StudentForm()
    else:
        form_var = StudentForm()
    return render(request, 'student_registration.html', {'form': form_var})


def student_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in sucessfully !!')
                return HttpResponseRedirect('student_dashboard')
    else:
        fm = AuthenticationForm()
    return render(request, 'student_login.html', {'form': fm})


def student_dashboard(request):
    if request.user.is_authenticated:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        return render(request, 'student_dashboard.html', {'username': request.user,
                                                          'hostname': hostname, 'IPAddr': IPAddr})

def view_attendance(request):
    var = ViewAttendance.objects.all().filter(username=request.user)
    present = len([i for i in var if i.attending])
    return render(request, 'view_attendance.html', {'username':request.user,'var' : var,'len':len(var),
                                                    'present':present,'absent':len(var)-present,
                                                    'avg':"{:.2f}".format((present/len(var)*100))})

def leave(request):
    return render(request, 'apply_for_leave.html', {'leave':LeaveForm})


def logout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('student_login')

