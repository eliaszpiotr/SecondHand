from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from application.models import CustomUser


class CustomUserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=64, widget=forms.TextInput(attrs={'placeholder': 'Email'}), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}), label='')
    first_name = forms.CharField(max_length=64,
                                 widget=forms.TextInput(attrs={'placeholder': 'First name'}),
                                 label='')
    last_name = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'placeholder': 'Last name'}), label='')

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

