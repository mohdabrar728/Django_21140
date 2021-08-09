from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .forms import MyForm


# Create your views here.
class ShowForm(FormView):
    form_class = MyForm
    template_name = 'text.html'
    success_url = 'printfrom'
    def form_valid(self,form):
        return super().form_valid(form)

class PrintForm(TemplateView):
    template_name = 'result.html'
    def post(self,*args,**kwargs):
        return
