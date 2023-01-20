from django.urls import path
from application.views import LandingPage, AddDonation, Register, ConfirmDonation, Logout, Login, Profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', LandingPage.as_view(), name='index'),
    path('add_donation/', AddDonation.as_view(), name='add_donation'),
    path('confirm/', ConfirmDonation.as_view(), name='confirmation'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='profile')
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)