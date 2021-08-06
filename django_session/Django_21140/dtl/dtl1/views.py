from django.shortcuts import render


# Create your views here.
def greet(req):
    return render(req, "home.html")


def bye(req):
    return render(req, "about.html",{'name' :'Abrar','age' : 'Only 24'})