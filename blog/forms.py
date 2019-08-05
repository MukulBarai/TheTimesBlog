from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from datetime import datetime, date
from .models import Post, Category

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)

class ProfileForm(ModelForm):
    date_joined = forms.DateTimeField(disabled=True)
    last_login = forms.DateTimeField(disabled=True)
    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login')