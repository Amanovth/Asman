from rest_framework import serializers

from .models import PartnerCategory, Partners


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ['title', 'description', 'img']


class DiscountListSerializer(serializers.ModelSerializer):
    partners = PartnersSerializer(many=True)

    class Meta:
        model = PartnerCategory
        fields = ['name', 'partners']
