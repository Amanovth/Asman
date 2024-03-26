from django.contrib import admin
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, UserStatuses
from src.payments.admin import BuyAsmanInline, PaymentsInline


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('referred_by', 'status', 'balance', 'username', 'first_name', 'last_name',
                           'email', 'phone', 'profile_photo', 'v_code', 'verified', 'qr',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('verified', 'v_code', 'qr', 'profile_photo')

    inlines = (BuyAsmanInline, PaymentsInline)


@admin.register(UserStatuses)
class UserStatusesAdmin(admin.ModelAdmin):
    list_display = ('standard', 'bronze', 'silver', 'gold', 'vip')

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False
