from rest_framework import generics

from .models import PartnerCategory, Partners
from .serializers import (
    DiscountListSerializer,
    PartnersSerializer
)


class DiscountListView(generics.ListAPIView):
    queryset = PartnerCategory.objects.all()
    serializer_class = DiscountListSerializer


class DiscountDetailView(generics.RetrieveAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
    lookup_field = 'id'
