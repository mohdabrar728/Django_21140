from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

User = get_user_model()
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class StudentForm(UserCreationForm):
    password2 = forms.CharField(label="confirm Password (again)", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': "Email"}
