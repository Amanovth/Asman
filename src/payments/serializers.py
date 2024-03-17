from rest_framework import serializers

from .models import (
    BuyAsman,
    WithdrawalAsman,
    Payment,
    Transfer,
    AsmanRate
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


class AsmanRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsmanRate
        fields = ['rate', 'standard', 'bronze', 'silver', 'gold']
