from django.urls import path
from .views import LandingPage, AddDonation, Login, Register

urlpatterns = [
    path('', LandingPage.as_view(), name='landing_page'),
    path('add_donation/', AddDonation.as_view(), name='add_donation'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    ]