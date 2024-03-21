from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from src.accounts.models import UserStatuses
from .models import (
    Stories,
    Wallets,
    AsmanRate
)
from .serializers import StoriesSerializers


class StoriesView(ListAPIView):
    queryset = Stories.objects.order_by("-id")
    serializer_class = StoriesSerializers


class AsmanDetailView(APIView):
    # permission_classes = [IsAuthenticated, ]

    def get(self, request):
        status = UserStatuses.objects.first()
        rate = AsmanRate.objects.first()
        wallets = Wallets.objects.first()

        # Combine serialized data into a single dictionary
        response_data = {
            'rate': rate.rate,
            'usdt': wallets.usdt,
            'asman': wallets.asman,
            'standard': status.standard,
            'bronze': status.bronze,
            'silver': status.silver,
            'gold': status.gold,
            'vip': status.vip
        }

        return Response(response_data)
