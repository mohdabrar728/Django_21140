from django.shortcuts import render
from . import models


# Create your views here.
def homeapp2(request):
    print(models.student)
    a = models.student.objects.all()
    return render(request, 'homeapp2.html', {'test': a })
