from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .our_forms import StudentForm
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
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
                hostname = socket.gethostname()
                IPAddr = socket.gethostbyname(hostname)
                return render(request, 'student_dashboard.html', {'username': fm.cleaned_data['username'],
                                                                  'hostname': hostname, 'IPAddr': IPAddr})
    else:
        fm = AuthenticationForm()
    return render(request, 'student_login.html', {'form': fm})
