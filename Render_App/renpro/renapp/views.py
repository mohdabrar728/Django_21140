from django.shortcuts import render

# Create your views here.
def showcase(req):
    return render(req, 'first.html')


def showcase1(req):
    return render(req, 'second.html')


def showcase2(req):
    return render(req, 'third.html')