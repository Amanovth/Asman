from rest_framework import generics
from rest_framework.response import Response

from .models import PartnerCategory, Partner
from .serializers import (
    PartnerDetailSerializer,
    CategoryListSerializer
)


class DiscountListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = PartnerCategory.objects.all()


class DiscountDetailView(generics.RetrieveAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerDetailSerializer
    lookup_field = 'id'
