from django.shortcuts import render,HttpResponse

# Create your views here.
def fapp(req):
    return HttpResponse('''first app page''')