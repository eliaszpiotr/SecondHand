from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from datetime import datetime


class MyAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        # if not first_name:
        #     raise ValueError('Users must have a first name')
        # if not last_name:
        #     raise ValueError('Users must have a last name')

        user = self.model(
            email=self.normalize_email(email),
            # first_name=first_name,
            # last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            # first_name=first_name,
            # last_name=last_name,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class Account(AbstractBaseUser):
    username = None
    email = models.EmailField(verbose_name='email', unique=True, max_length=64)
    first_name = models.CharField(verbose_name='first name', max_length=50)
    last_name = models.CharField(verbose_name='last name', max_length=50)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

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
        return self.name, self.type


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
