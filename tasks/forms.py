# tasks/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # `password1` and `password2` are already part of `UserCreationForm`

    # No need to override the `clean()` method as `UserCreationForm` already validates passwords


class LoginForm(AuthenticationForm):
    # The AuthenticationForm already contains the `username` and `password` fields, so you don't need to redefine them.
    pass
