from django import forms
from django.contrib.auth.models import User
from .models import Client


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class RegistrationForm(forms.ModelForm):
    age = forms.IntegerField(required=True)
    phone = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

    def save(self):
        age = self.cleaned_data["age"]
        num = self.cleaned_data["phone"]
        self.cleaned_data.pop('age')
        self.cleaned_data.pop('phone')
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        client = Client.objects.create(user=user, age=age, number=num)
        client.save()
        return user
