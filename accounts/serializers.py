import random
from rest_framework import serializers

from .models import User
from .services import send_verification_mail


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    v_code = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'v_code'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2')
        validated_data['v_code'] = str(random.randint(100000, 999999))

        user = User(**validated_data, password=password)
        user.set_password(password)
        user.save()
        send_verification_mail(validated_data)
        return user
    

class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    v_code = serializers.IntegerField()

    class Meta:
        fields = ['email', 'v_code']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        fields = ['email', 'password']