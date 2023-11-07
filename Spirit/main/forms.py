from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Client


class LoginForm(AuthenticationForm):
    class Meta:
        model = Client
        fields = ('login','password')


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ['name','age', 'number', 'login' ,'password']

