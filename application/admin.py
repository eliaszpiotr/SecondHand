from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Donation, Institution, Category


@admin.register(Account)
class AccountAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

    filter_horizontal = ()
    fieldsets = ()


@admin.register(Institution)
class Institution(admin.ModelAdmin):
    list_display = ('name', 'type',)
    search_fields = ('name',)
    list_filter = ('type',)

    filter_horizontal = ()
    fieldsets = ()


@admin.register(Donation)
class Donation(admin.ModelAdmin):
    list_display = ('user', 'quantity', 'institution', 'address', 'phone_number', 'city', 'zip_code', 'pick_up_date', 'pick_up_time', 'pick_up_comment')
    search_fields = ('user',)
    list_filter = ('institution',)

    filter_horizontal = ()
    fieldsets = ()
