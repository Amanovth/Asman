from django.urls import path

from .views import (
    ScannerView,
    BuyAsmanView,
    # DepositView,
    # WithdrawalView,
    AsmanRateView,
    PaymentHistoryView
)

urlpatterns = [
    # Payments
    path('scanner/', ScannerView.as_view(), name='payment-scan'),
    path('buy-asman/', BuyAsmanView.as_view(), name='payment-buy-asman'),
    # path('payment/deposit/', DepositView.as_view(), name='payment-deposit'),
    # path('payment/withdrawal/', WithdrawalView.as_view(), name='payment-withdrawal'),
    path('asman-rate/', AsmanRateView.as_view(), name='payment-asman-rate'),
    path('history/', PaymentHistoryView.as_view(), name='payment-history')
]
