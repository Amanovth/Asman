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
    readonly_fields = ('img',)


class PaymentsInline(admin.StackedInline):
    model = Payment
    extra = 0


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('balance', 'username', 'first_name', 'last_name',
                           'email', 'phone', 'profile_photo', 'v_code', 'verified', 'qr', 'is_active')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    inlines = (BuyAsmanInline, PaymentsInline)


@admin.register(BuyAsman)
class BuyAsmanAdmin(admin.ModelAdmin):
    list_display = ('user', 'operation_time', 'status', 'processed')
    readonly_fields = ('img', 'user')
    list_filter = ('status', 'processed')

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


admin.site.register(WithdrawalAsman)
admin.site.register(Transfer)
admin.site.unregister(Group)
