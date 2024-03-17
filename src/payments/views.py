from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import (
    BuyAsman,
    WithdrawalAsman,
    Payment,
    Transfer
)
from .serializers import (
    TransferSerializer,
    PaymentSerializer,
    BuyAsmanSerializer
)


class ScannerView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get_serializer_class(self):
        payment_type = self.request.query_params.get('type')

        if payment_type == '1':
            return TransferSerializer
        return PaymentSerializer

    def post(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            if request.query_params.get('type') == '1':
                # If the type is 1, it's a Transfer
                # Set the payer as the current user
                serializer.validated_data['payer'] = request.user
                serializer.save()
            else:
                # If the type is not 1, it's a Payment
                # Set the user as the current user
                serializer.validated_data['user'] = request.user
                serializer.save()

            return Response({'response': True})
        else:
            return Response(serializer.errors)


class BuyAsmanView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = BuyAsman.objects.all()
    serializer_class = BuyAsmanSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)