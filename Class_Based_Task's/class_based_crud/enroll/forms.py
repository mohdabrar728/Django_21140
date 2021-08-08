from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
 class Meta:
  model = User
  fields = ['email', 'subject', 'mail']
  widgets = {
   'email': forms.EmailInput(attrs={'class':'form-control'}),
   'subject': forms.TextInput(attrs={'class': 'form-control'}),
   'mail': forms.Textarea(attrs={'class': 'form-control'}),
  }