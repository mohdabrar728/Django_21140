from django.shortcuts import render,HttpResponse

# Create your views here.
def viewer(request):
    return HttpResponse("<h1 align:12px dotted ></h1>")