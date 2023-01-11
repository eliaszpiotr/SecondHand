from django.shortcuts import render
from django.views import View


class LandingPage(View):
    def get(self, request):
        return render(request, 'application/index.html')


class AddDonation(View):
    def get(self, request):
        return render(request, 'application/form.html')


class Login(View):
    def get(self, request):
        return render(request, 'application/login.html')


class Register(View):
    def get(self, request):
        return render(request, 'application/register.html')


