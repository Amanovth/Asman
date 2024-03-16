from django.contrib import admin
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import (
    User,
    BuyAsmanRequest,
    Payments
)


class BuyAsmanRequestInline(admin.StackedInline):
    model = BuyAsmanRequest
    extra = 0
    readonly_fields = ('screenshot',)


class PaymentsInline(admin.StackedInline):
    model = Payments
    extra = 0


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('is_active', 'coins', 'username', 'first_name', 'last_name',
        'email', 'phone', 'profile_photo', 'v_code', 'verified', 'qr')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    inlines = (BuyAsmanRequestInline, PaymentsInline)


@admin.register(BuyAsmanRequest)
class BuyAsmanAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'status', 'processed')
    readonly_fields = ('screenshot', 'user')
    list_filter = ('status', 'processed')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('user',)

    # def has_delete_permission(self, request, obj=None):
    #     return False

    # def has_add_permission(self, request):
    #     return False

admin.site.unregister(Group)
