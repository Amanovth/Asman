from rest_framework import serializers

from .models import PartnerCategory, Partner


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'title', 'description', 'img']


class DiscountListSerializer(serializers.ModelSerializer):
    partners = PartnersSerializer(many=True)

    class Meta:
        model = PartnerCategory
        fields = ['name', 'partners']
