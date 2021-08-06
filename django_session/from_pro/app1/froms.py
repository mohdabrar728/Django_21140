from django import forms

class Student(forms.Form):
    name = forms.CharField(max_length=70)
    email = forms.EmailField(max_length=70,help_text = "text")
    CHOICES = [('1', 'male'), ('2', 'Female')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    human = forms.CharField(widget=forms.CheckboxInput)
    geeks_field = forms.ImageField()
    video = forms.MultiWidget(widgets=forms.Media)
