from django.http import HttpResponseRedirect
from django.shortcuts import render
from .froms import Fclass
from .models import LM_Model
from datetime import datetime, timedelta

# Create your views here.
def show(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            fm = Fclass(req.POST)
            if fm.is_valid():
                book_name = fm.cleaned_data['book_name']
                author_name = fm.cleaned_data['author_name']
                category = fm.cleaned_data['category']
                ISBN = fm.cleaned_data['ISBN']
                quantity = fm.cleaned_data['quantity']
                store = LM_Model(book_name=book_name, author_name=author_name, category=category,
                                 ISBN=ISBN, quantity=quantity)
                store.save()
                fm = Fclass()
        else:
            fm = Fclass()
        return render(req, "index.html", {'form': Fclass, 'data': LM_Model.objects.all()})
    else:
        return HttpResponseRedirect('/login')

def udata(req, id):
    if req.method == 'POST':
        pi = LM_Model.objects.get(pk=id)
        fa = Fclass(req.POST, instance=pi)
        if fa.is_valid():
            fa.save()
    else:
        pi = LM_Model.objects.get(pk=id)
        fa = Fclass(instance=pi)
    return render(req,"edit.html", {'form1': fa})


def ddata(req, id):
    if req.method == 'POST':
        pi = LM_Model.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/app1/show')
