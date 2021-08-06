from django.shortcuts import render
def home(request):
    return render(request,'st1/home.html',{'msg':'abrar'})