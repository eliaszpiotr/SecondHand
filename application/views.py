from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from application.models import Donation


class LandingPage(View):

    def get(self, request):
        bags = 0
        donations = Donation.objects.all()
        for donation in donations:
            bags += donation.quantity
        organizations = Donation.objects.values('institution').distinct().count()
        context = {
            'bags': bags,
            'organizations': organizations,
        }
        return render(request, 'application/index.html', context)


class AddDonation(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'application/form.html')


class ConfirmDonation(View):
    def get(self, request):
        return render(request, 'application/form-confirmation.html')


class Login(View):
    def get(self, request):
        return render(request, 'application/login.html')


class Register(View):
    def get(self, request):
        return render(request, 'application/register.html')


