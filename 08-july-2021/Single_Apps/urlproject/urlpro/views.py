from django.shortcuts import render,HttpResponse

# Create your views here.
def pro(request):
    return HttpResponse('''<h1 align=center style="border:12px double green"''')