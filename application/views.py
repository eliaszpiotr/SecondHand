from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from application.models import Donation, Institution, Category


class LandingPage(View):

    def get(self, request):
        bags = 0
        donations = Donation.objects.all()
        for donation in donations:
            bags += donation.quantity
        organizations = Donation.objects.values('institution').distinct().count()
        foundations = Institution.objects.all().filter(type='Foundation')
        non_gov_orgs = Institution.objects.all().filter(type='Non-governmental organization')
        local_collections = Institution.objects.all().filter(type='Local collection')
        context = {
            'bags': bags,
            'organizations': organizations,
            'foundations': foundations,
            'non_gov_orgs': non_gov_orgs,
            'local_collections': local_collections,
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


