from django.contrib import admin
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import (
    User,
    BuyAsman,
    Payment,
    WithdrawalAsman,
    Transfer
)


class BuyAsmanInline(admin.StackedInline):
    model = BuyAsman
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class PaymentsInline(admin.StackedInline):
    model = Payment
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('balance', 'username', 'first_name', 'last_name',
                           'email', 'phone', 'is_active', 'profile_photo', 'v_code', 'verified', 'qr',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('verified', 'v_code', 'qr', 'profile_photo')

    inlines = (BuyAsmanInline, PaymentsInline)


@admin.register(BuyAsman)
class BuyAsmanAdmin(admin.ModelAdmin):
    list_display = ('user', 'operation_time', 'status',)
    readonly_fields = ('img', 'operation_time')
    list_filter = ('status',)

    # def has_delete_permission(self, request, obj=None):
    #     return False
    #
    # def has_add_permission(self, request):
    #     return False


@admin.register(Payment)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('user',)

    # def has_delete_permission(self, request, obj=None):
    #     return False

    # def has_add_permission(self, request):
    #     return False


@admin.register(WithdrawalAsman)
class WithdrawalAsmanAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'status', 'operation_time')
    readonly_fields = ('operation_time',)


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('payer', 'recipient', 'amount', 'operation_time')
    readonly_fields = ('operation_time',)


admin.site.unregister(Group)
