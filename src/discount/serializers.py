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
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = ['id', 'title', 'description', 'img', 'days', 'discount',]

    def get_days(self, obj):
        user = self.context['request'].user
        status = user.status
        payments = Payment.objects.filter(partner=obj, user=user)

        if not payments.exists():
            return True

        days_from_last_payment = (timezone.now() - payments.order_by('-operation_time').first().operation_time).days

        days = 0

        if status == 'Стандарт':
            days = obj.v_standard - days_from_last_payment
        if status == 'Бронза':
            days = obj.v_bronze - days_from_last_payment
        if status == 'Серебро':
            days = obj.v_silver - days_from_last_payment
        if status == 'Золото':
            days = obj.v_gold - days_from_last_payment
        if status == 'VIP':
            days = obj.v_vip - days_from_last_payment

        if days <= 0:
            return True
        return days

    def get_discount(self, obj):
        user = self.context['request'].user
        status = user.status

        if status == 'Стандарт':
            return obj.d_standard
        if status == 'Бронза':
            return obj.d_bronze
        if status == 'Серебро':
            return obj.d_silver
        if status == 'Золото':
            return obj.d_gold
        if status == 'VIP':
            return obj.d_vip