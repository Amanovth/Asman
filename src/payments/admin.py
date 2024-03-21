from django.contrib import admin
from django.contrib.auth.models import Group

from .models import (
    BuyAsman,
    Payment,
    WithdrawalAsman,
    Transfer,
    AsmanRate,
    History
)


@admin.register(AsmanRate)
class AsmanRateAdmin(admin.ModelAdmin):
    list_display = ('rate', 'standard', 'bronze', 'silver', 'gold', 'vip')

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
    list_display = ('user', 'amount', 'operation_time', 'status', 'processed')
    readonly_fields = ('img', 'operation_time',)
    list_filter = ('status', 'processed')

    fields = ('status', 'amount', 'user', 'img', 'operation_time')

    # def has_delete_permission(self, request, obj=None):
    #     return False
    #
    # def has_add_permission(self, request):
    #     return False


@admin.register(WithdrawalAsman)
class WithdrawalAsmanAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'operation_time', 'status', 'processed')
    readonly_fields = ('operation_time',)
    fields = ('status', 'amount', 'user', 'address', 'operation_time')


@admin.register(Payment)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'partner', 'operation_time')
    # readonly_fields = ('operation_time',)

    # def has_delete_permission(self, request, obj=None):
    #     return False

    # def has_add_permission(self, request):
    #     return False


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('payer', 'recipient', 'amount', 'operation_time')
    readonly_fields = ('operation_time',)


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'info', 'get_recipient', 'total', 'operation_time')
    readonly_fields = ('user', 'info', 'total', 'operation_time', 'partner', 'recipient')

    def get_recipient(self, object):
        if object.recipient:
            return f'{object.recipient.first_name} {object.recipient.last_name[0]}'
        return object.partner

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(self.readonly_fields)
        if not obj or (not obj.partner and not obj.recipient):
            readonly_fields.append('status')
        return readonly_fields

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def has_add_permission(self, request):
        return False

    get_recipient.short_description = 'Имя получателя'


admin.site.unregister(Group)
