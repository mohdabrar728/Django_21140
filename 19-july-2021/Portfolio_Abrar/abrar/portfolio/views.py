from django.shortcuts import render
from .models import Data
# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def resume(request):
    return render(request, "resume.html")

def project(request):
    return render(request, "project.html")

def research_paper(request):
    return render(request, "research_paper.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("mail")
        msg = request.POST.get("message")
        b = Data(name=name,email=email,msg=msg)
        b.save()
    return render(request, "contact.html")