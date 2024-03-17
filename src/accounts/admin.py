from django.contrib import admin
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User
from src.payments.admin import BuyAsmanInline, PaymentsInline


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('balance', 'username', 'first_name', 'last_name',
                           'email', 'phone', 'profile_photo', 'v_code', 'verified', 'qr',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('verified', 'v_code', 'qr', 'profile_photo')

    inlines = (BuyAsmanInline, PaymentsInline)


# admin.site.unregister(Group)
