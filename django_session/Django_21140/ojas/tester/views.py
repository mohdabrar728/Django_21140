from django.shortcuts import render, HttpResponse


# Create your views here.
def greeting(request):
    return HttpResponse("""<h1 align=center style="color:cyan ;border:solid blue;border-style:dashed;margin:50px 50px 0px 50px ;padding:20px">
    Hello Swetha <h1 align=center style="color:green ;border:solid blue;border-style:dashed;margin:0px 50px 50px 50px;padding:20px">Welcome Django World</h1>""")


def bye(request):
    return HttpResponse("""<h1 align=center style="color:cyan ;border:solid blue;border-style:dashed;margin:50px 50px 0px 50px ;padding:20px">
    Hello Swetha <h1 align=center style="color:green ;border:solid yellow;border-style:dashed;margin:0px 50px 50px 50px;padding:20px">Good Bye Django World</h1>""")
