from django.shortcuts import render,HttpResponse

# Create your views here.
def firstview(resquest):
    return HttpResponse("""<h1 align='center' style='color:red;border:12px double black'>First View</h1>""")

def secondview(resquest):
    return HttpResponse("""<h1 align='center' style='color:cyan;border:12px double blue'>Second View</h1>""")

def thirdview(resquest):
    return HttpResponse("""<h1 align='center' style='color:hotpink;border:12px double orange'>Third View</h1>""")