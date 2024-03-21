from datetime import timedelta
from django.utils import timezone
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.db.models.functions import TruncDate
from django.db.models import Count

from .models import (
    BuyAsman,
    WithdrawalAsman,
    Payment,
    Transfer,
    History
)
from .serializers import (
    TransferSerializer,
    PaymentSerializer,
    BuyAsmanSerializer,
    PaymentHistorySerializer,
    WithdrawalSerializer
)


class ScannerView(generics.GenericAPIView):
    # permission_classes = [permissions.IsAuthenticated, ]

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
            return Response({'response': False})


class BuyAsmanView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = BuyAsman.objects.all()
    serializer_class = BuyAsmanSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'response': True})
        return Response({'response': False})


class PaymentHistoryView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = PaymentHistorySerializer

    def get_queryset(self):
        days = timezone.now() - timedelta(days=int(self.request.query_params.get('days')))
        return History.objects.filter(user=self.request.user, operation_time__gte=days).annotate(
            date=TruncDate('operation_time')).values('date').annotate(history_list=Count('pk')).order_by('-date')

    def list(self, request, *args, **kwargs):
        serialized_data = []
        for entry in self.get_queryset():
            history_objects = History.objects.filter(user=self.request.user, operation_time__date=entry['date'])
            serialized_history = self.serializer_class(history_objects, many=True).data
            serialized_data.append({'date': entry['date'].strftime('%d.%m.%Y'), 'list': serialized_history})
        return Response(serialized_data)


class WithdrawalView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = WithdrawalAsman.objects.all()
    serializer_class = WithdrawalSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'response': True})
        return Response({'response': False})
