from rest_framework import generics

from .models import PartnerCategory
from .serializers import (
    DiscountListSerializer
)


class DiscountListView(generics.ListAPIView):
    queryset = PartnerCategory.objects.all()
    serializer_class = DiscountListSerializer
