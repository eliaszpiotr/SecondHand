from django import forms
from django.contrib.auth.forms import UserCreationForm

from application.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=64, help_text='Add a valid email address.')

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')



