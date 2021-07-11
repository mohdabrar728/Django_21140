from django.shortcuts import render,HttpResponse

# Create your views here.
def sapp(req):
    return HttpResponse('''second app page''')