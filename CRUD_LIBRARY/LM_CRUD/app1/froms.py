from django import forms
from .models import LM_Model


class Fclass(forms.ModelForm):
    class Meta:
        model = LM_Model
        fields = ['book_name', 'author_name', 'category', 'ISBN', 'quantity']
        widgets = {
            'book_name': forms.TextInput(attrs={'class': "",
                                                'placeholder': 'Enter Book Name'}),
            'author_name': forms.TextInput(attrs={'class': "",
                                                  'placeholder': 'Enter Author Name'}),
            'category': forms.TextInput(attrs={'class': "",
                                               'placeholder': 'Enter Category of Book'}),
            'ISBN': forms.TextInput(attrs={'class': "",
                                           'placeholder': 'Enter ISBN'}),
            'quantity': forms.TextInput(attrs={'class': "",
                                               'placeholder': 'Enter Quantity'}),
        }
