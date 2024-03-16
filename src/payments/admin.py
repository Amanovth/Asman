from django.contrib import admin
from django.contrib.auth.models import Group

from .models import (
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
