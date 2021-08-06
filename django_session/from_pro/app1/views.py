from django.shortcuts import render
from .froms import Student
# Create your views here.
def show(req):
    pull = Student(label_suffix=' : '   )
    return render(req, "test.html", {'stu':pull})

def show1(req):
    return render(req, "base.html")

def te(req):
    pull = Student(label_suffix=' : '   )
    return render(req, "te.html", {'stu':pull})