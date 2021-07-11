from django.shortcuts import render,HttpResponse

# Create your views here.
def saview(req):
    return HttpResponse('''<h1 align=center>Second App Intial View</h1>''')

def saview1(req):
    return HttpResponse('''<h1 align=center>Second App First View</h1>''')

def saview2(req):
    return HttpResponse('''<h1 align=center>Second App Second View</h1>''')
