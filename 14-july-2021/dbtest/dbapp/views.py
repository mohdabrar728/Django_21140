from django.shortcuts import render
from . import models
# Create your views here.
def tester(request):
    return render(request, 'test.html',{"db":models.Stroge})