from collections import defaultdict
from rest_framework import serializers

from .models import (
    BuyAsman,
    WithdrawalAsman,
    Payment,
    Transfer,
    History
)


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['partner', ]


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['recipient', 'amount']


class BuyAsmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyAsman
        fields = ['img', ]


class PaymentHistorySerializer(serializers.ModelSerializer):
    recipient = serializers.SerializerMethodField()
    operation_time = serializers.SerializerMethodField()

    class Meta:
        model = History
        fields = ['recipient', 'info', 'total', 'operation_time', 'status']

    def get_recipient(self, obj):
        if obj.recipient:
            return f'{obj.recipient.first_name} {obj.recipient.last_name[0]}'
        elif obj.partner:
            return obj.partner.title
        return False

    def get_operation_time(self, obj):
        return obj.operation_time.strftime("%d.%m.%Y, %H:%M")


class WithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = WithdrawalAsman
        fields = ['address', 'amount']
