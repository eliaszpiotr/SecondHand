from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from application.models import CustomUser
from django.contrib.auth import get_user_model


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


class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='', help_text='password')

    class Meta:
        model = get_user_model()
        fields = ('email', 'password')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email does not exist.")
        return email


