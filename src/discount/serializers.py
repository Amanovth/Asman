from rest_framework import serializers
from django.utils import timezone

from src.payments.models import Payment
from .models import PartnerCategory, Partner


class PartnersSerializer(serializers.ModelSerializer):
    days = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = ['id', 'title', 'description', 'img', 'days']

    def get_days(self, obj):
        last_payment = Payment.objects.filter(partner=obj)

        if not last_payment.exists():
            return True

        return (timezone.now() - last_payment.order_by('-operation_time').first().operation_time).days


class DiscountListSerializer(serializers.ModelSerializer):
    partners = PartnersSerializer(many=True)

    class Meta:
        model = PartnerCategory
        fields = ['name', 'partners']
