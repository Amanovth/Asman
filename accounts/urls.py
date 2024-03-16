from django.urls import path

from .views import (
    RegisterView,
    VerifyEmailView,
    LoginView,
    ForgotPasswordView,
    UserInfoView,
)
from .payment_views import (
    ScannerView,
    BuyAsmanView,
    # DepositView,
    # WithdrawalView,
)

urlpatterns = [
    # Authentication
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/verify-email/', VerifyEmailView.as_view(), name='auth-verify-email'),
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('auth/forgot-password/', ForgotPasswordView.as_view(), name='auth-forgot-password'),
    path('auth/user-info/', UserInfoView.as_view(), name='auth-user-info'),

    # Payments
    path('payment/scanner/', ScannerView.as_view(), name='payment-scan'),
    path('payment/buy-asman/', BuyAsmanView.as_view(), name='payment-buy-asman')
    # path('payment/deposit/', DepositView.as_view(), name='payment-deposit'),
    # path('payment/withdrawal/', WithdrawalView.as_view(), name='payment-withdrawal'),
]
