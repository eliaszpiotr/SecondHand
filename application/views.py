from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView
from application.models import Donation, Institution, Category, CustomUser, CustomUserManager
from application.forms import CustomUserRegisterForm


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


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class Register(CreateView):
    model = CustomUser
    form_class = CustomUserRegisterForm
    template_name = 'application/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class Login(View):
    def get(self, request):
        return render(request, 'login.html')


