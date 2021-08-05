from django import forms

CHOICES = (
    ("1", "shivani"),
    ("2", "rassu"),
    ("3", "swetha"),
    ("4", "teju"),
    ("5", "abrar"),
)
CHOICES2=[('select1','Female'),
         ('select2','Male')]

class StuForms(forms.ModelForm):
    class Meta:
        model = ModForms
        fields = '__all__'