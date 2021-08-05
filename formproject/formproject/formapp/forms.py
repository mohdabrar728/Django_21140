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

class StuForms(forms.Form):
    name = forms.CharField(label='Your Name',label_suffix=':', initial='mr/mrs', max_length=30)
    email = forms.EmailField(max_length=30)
    passwd = forms.CharField(widget=forms.PasswordInput, max_length=10)
    id = forms.IntegerField(max_value=40)
    subject = forms.CharField(max_length=100, help_text='100 characters max.')
    url = forms.URLField(initial='http://')
    contact = forms.IntegerField(max_value=40)
    sname = forms.CharField(widget=forms.HiddenInput())
    message = forms.CharField(widget=forms.Textarea)
    time = forms.DateTimeField()
    checkbox = forms.BooleanField()
    null = forms.NullBooleanField()

    choice = forms.ChoiceField(choices=CHOICES)
    like = forms.ChoiceField(choices=CHOICES2, widget=forms.RadioSelect)