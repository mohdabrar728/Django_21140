from django.shortcuts import render
from .models import Teacher
# Create your views here.
def teacher(request):
    if request.method == "POST":
        uid = request.POST.get("uid")
        tid = request.POST.get("id")
        name = request.POST.get("name")
        age = request.POST.get("age")
        sub = request.POST.get("sub")
        data = Teacher(uid=uid, tid=tid, name=name, age=age, sub=sub)
        data.save()
    return render(request, "app1.html", {"data":Teacher.objects.all()})

