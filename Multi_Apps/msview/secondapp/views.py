from django.shortcuts import render,HttpResponse

# Create your views here.
def secondappview(request):
    return HttpResponse('''<h1 align='center' style='color:red'>Second App View</h1>''')