from django.urls import path

from .views import (
    ScannerView,
    BuyAsmanView,
    # DepositView,
    # WithdrawalView,
    PaymentHistoryView,
    WithdrawalView
)

urlpatterns = [
    # Payments
    path('scanner/', ScannerView.as_view(), name='payment-scan'),
    path('buy-asman/', BuyAsmanView.as_view(), name='payment-buy-asman'),
    # path('payment/deposit/', DepositView.as_view(), name='payment-deposit'),
    path('withdrawal/', WithdrawalView.as_view(), name='payment-withdrawal'),
    path('history/', PaymentHistoryView.as_view(), name='payment-history')
]
