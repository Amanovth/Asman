import random
from rest_framework import serializers

from .models import User
from .services import send_verification_mail, calculate_user_status

from src.payments.models import AsmanRate


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    v_code = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',
            'v_code'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError(
                {'password': 'Пароли не совпадают'})
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('confirm_password')
        validated_data['v_code'] = str(random.randint(100000, 999999))

        user = User(**validated_data, password=password)
        user.set_password(password)
        user.save()
        send_verification_mail(validated_data)
        return user


class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    v_code = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        fields = ['email', 'password']


class UserInfoSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone',
                  'profile_photo', 'balance', 'status', 'qr']

    def get_status(self, obj):
        asman_rate = AsmanRate.objects.first()

        return calculate_user_status(obj.balance, asman_rate)


class UpdatePhotoSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField(required=True)

    class Meta:
        model = User
        fields = ['profile_photo', ]
