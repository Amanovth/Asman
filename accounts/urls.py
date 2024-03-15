from django.urls import path

from .views import (
    RegisterView,
    VerifyEmailView,
    LoginView,
    ForgotPasswordView,
    UserInfoView
)

urlpatterns = [
    path('register', RegisterView.as_view(), name='auth-register'),
    path('verify-email', VerifyEmailView.as_view(), name='auth-verify-email'),
    path('login', LoginView.as_view(), name='auth-login'),
    path('forgot-password', ForgotPasswordView.as_view(), name='auth-forgot-password'),
    path('user-info', UserInfoView.as_view(), name='auth-user-info')
]