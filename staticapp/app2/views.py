from django.shortcuts import render

# Create your views here.
def homeapp2(request):
    return render(request, 'homeapp2.html')