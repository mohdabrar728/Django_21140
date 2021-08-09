from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=75)
    age = forms.IntegerField()
    vaccine = forms.CharField(max_length=75)