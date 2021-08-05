from django.shortcuts import render,HttpResponse

# Create your views here.
def fun_home(request):
    return render(request,"home.html")

def fun_blog(request):
    return render(request,"blog.html")

def fun_players(request):
    return render(request,"players.html")

def fun_football(request):
    return render(request,"football.html")

def fun_cricket(request):
    return render(request,"cricket.html")

