from rest_framework import generics
from rest_framework.response import Response

from .models import PartnerCategory, Partner, Status
from .serializers import (
    DiscountListSerializer,
    PartnerSerializer
)


class DiscountListView(generics.ListAPIView):
    serializer_class = DiscountListSerializer
    queryset = Status.objects.all()


class DiscountDetailView(generics.RetrieveAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    lookup_field = 'id'
