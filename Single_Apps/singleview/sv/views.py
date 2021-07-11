from django.shortcuts import render,HttpResponse

# Create your views here.
def firstview(request):
    return HttpResponse("""<h1 align='center' style='color:red;border:12px double black'>First View</h1>""")