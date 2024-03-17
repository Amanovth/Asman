from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

from .models import User
from .services import generate_password, forgot_password
from .serializers import (
    RegisterSerializer,
    VerifyEmailSerializer,
    LoginSerializer,
    UserInfoSerializer
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'response': True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class VerifyEmailView(generics.GenericAPIView):
    serializer_class = VerifyEmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            v_code = serializer.validated_data.get('v_code')
            email = serializer.validated_data.get('email')

            try:
                user = User.objects.get(email=email)
            except ObjectDoesNotExist:
                return Response({'response': False})

            if user.v_code == v_code:
                user.verified = True
                user.v_code = None
                user.save()

                return Response({'response': True, 'token': user.token()})
            return Response({'response': False, 'message': 'Введен неверный код'})
        return Response(serializer.errors)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            if user.verified:
                return Response({
                    'response': True,
                    'token': user.token(),
                })
            return Response({
                'response': False,
                'message': 'Потвердите адрес электронной почты',
            })
        return Response({
            'response': False,
            'message': 'Невозможно войти в систему с указанными учетными данными',
        })


class ForgotPasswordView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            return Response({
                'response': False,
                'message': 'Пользователь с таким адресом электронной почты не существует'
            })

        password = generate_password()
        user.set_password(password)
        user.save()

        forgot_password(email, password)

        return Response({'response': True})


class UserInfoView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        serializer = UserInfoSerializer(request.user)
        return Response(serializer.data)


class ChangePasswordView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if new_password != confirm_password:
            return Response({'response': False, 'message': 'Новый пароль и подтверждение пароля не совпадают.'})

        if not check_password(old_password, user.password):
            return Response({'response': False, 'message': 'Текущий пароль неверен'})

        user.set_password(new_password)
        user.save()

        return Response({'response': True})
