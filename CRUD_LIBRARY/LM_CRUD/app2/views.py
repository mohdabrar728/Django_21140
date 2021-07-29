from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.
def sign_up(request):
    if request.method=="POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created successfully')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request,'signup.html',{'form':fm})
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged Successfully ')
                    return HttpResponseRedirect('/app1/show')
        else:
            fm = AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/app1/show')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def user_change_pass(request):
    if request.method=="POST":
        fm=PasswordChangeForm(user=request.user,data=request.post)
        if fm.is_valid():
            update_session_auth_hash(request,fm.user)
            return HttpResponseRedirect('/app1/show')
    else:
        fm=PasswordChangeForm(user=request.user)
    return render(request,'change.html',{'form':fm})
