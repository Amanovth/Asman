from rest_framework import serializers
from django.utils import timezone

from src.payments.models import Payment
from .models import PartnerCategory, Partner


class PartnerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'title', 'description', 'img',
                  'd_standard', 'd_bronze', 'd_silver', 'd_gold', 'd_vip']


class CategoryListSerializer(serializers.ModelSerializer):
    partners = PartnerListSerializer(many=True)

    class Meta:
        model = PartnerCategory
        fields = ['name', 'partners']


class PartnerDetailSerializer(serializers.ModelSerializer):
    days = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = ['id', 'title', 'description', 'img', 'days',
                  'v_standard', 'v_bronze', 'v_silver', 'v_gold', 'v_vip']

    def get_days(self, obj):
        user = self.context['request'].user
        last_payment = Payment.objects.filter(partner=obj, user=user)

        if not last_payment.exists():
            return True

        return (timezone.now() - last_payment.order_by('-operation_time').first().operation_time).days
