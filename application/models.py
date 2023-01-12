from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import datetime


class MyAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class Account(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email', unique=True, max_length=64)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # sprawdzic!!!
    # REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    class Type(models.TextChoices):
        FOUNDATION = 'Foundation'
        NGO = 'Non-governmental organization'
        LOCAL = 'Local collection'

    type = models.CharField(max_length=64, choices=Type.choices, default=Type.FOUNDATION)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.name}, {self.type}'


class Donation(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='quantity')
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=9)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField(verbose_name='pick up date', default=datetime.now)
    pick_up_time = models.TimeField(verbose_name='pick up time', default=datetime.now)
    pick_up_comment = models.TextField(verbose_name='pick up comment', blank=True)
