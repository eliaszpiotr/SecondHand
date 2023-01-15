from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView
from application.models import Donation, Institution, Category, CustomUser, CustomUserManager
from application.forms import CustomUserRegisterForm, CustomUserLoginForm


class LandingPage(View):

    def get(self, request):
        """
        This method is responsible for rendering the home page.
        """
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
        categories = Category.objects.all().order_by('name')
        organisations = Institution.objects.all().order_by('name')
        context = {
            'categories': categories,
            'organisations': organisations,
        }

        return render(request, 'application/form.html', context)


class ConfirmDonation(View):
    def get(self, request):
        return render(request, 'application/form-confirmation.html')


class Register(CreateView):
    model = CustomUser
    form_class = CustomUserRegisterForm
    template_name = 'application/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class Login(LoginView):
    template_name = 'application/login.html'
    authentication_form = CustomUserLoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        # Log custom information about the user here
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('index')


class Logout(LogoutView):
    template_name = 'application/index.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')



