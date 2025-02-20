from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import customerUser

class customerUserCreationForm(UserCreationForm):
    class Meta:
        model = customerUser
        fields = ('username', 'email', 'phone', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = customerUser
        fields = ('username', 'password')