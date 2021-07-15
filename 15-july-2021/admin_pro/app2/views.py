from django.shortcuts import render
from .models import Student
# Create your views here.
def student(request):
    if request.method == "POST":
        uid = request.POST.get("uid")
        sid = request.POST.get("id")
        name = request.POST.get("name")
        age = request.POST.get("age")
        cls = request.POST.get("cls")
        data = Student(uid=uid, sid=sid, name=name, age=age, cls=cls)
        data.save()
    return render(request, "app2.html", {'data':Student.objects.all()})

