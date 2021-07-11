from django.shortcuts import render,HttpResponse

# Create your views here.
def firstappview(request):
    return HttpResponse('''<h1 align='center'>First App View</h1>''')
