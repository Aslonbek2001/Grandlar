from django.forms import Form
from django import forms


class LoginForm(Form):
    username = forms.CharField()
    password = forms.PasswordInput()
