from django.contrib import admin
from django.contrib.auth.models import Group

from .models import (
    BuyAsman,
    Payment,
    WithdrawalAsman,
    Transfer,
    AsmanRate
)


@admin.register(AsmanRate)
class AsmanRateAdmin(admin.ModelAdmin):
    list_display = ('rate', 'standard', 'bronze', 'silver', 'gold')

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


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
    list_display = ('user', 'operation_time', 'status', 'processed')
    readonly_fields = ('img', 'operation_time', 'user')
    list_filter = ('status', 'processed')

    fields = ('status', 'amount', 'user', 'img', 'operation_time')

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
