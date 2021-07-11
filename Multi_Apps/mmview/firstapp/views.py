from django.shortcuts import render,HttpResponse

# Create your views here.
def faview(req):
    return HttpResponse('''<h1 align=center>First App Intial View</h1>''')

def faview1(req):
    return HttpResponse('''<h1 align=center>First App First View</h1>''')

def faview2(req):
    return HttpResponse('''<h1 align=center>First App Second View</h1>''')
