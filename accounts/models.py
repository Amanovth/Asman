import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token

from .managers import CustomUserManager


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        max_length=36
    )
    qr = models.ImageField(
        'QR', 
        null=True, blank=True,
        editable=False,
    )
    username = models.CharField(
        _("username"),
        max_length=150,
        # unique=True,
        blank=True,
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    phone = models.CharField(
        'Телефон',
        max_length=255,
        blank=True
    )
    email = models.EmailField(
        'Email',
        unique=True
    )
    v_code = models.CharField(
        'Код подтверждения',
        null=True, blank=True,
        max_length=6
    )
    verified = models.BooleanField(
        'Подтверждено',
        default=False
    )
    coins = models.FloatField(
        'Количество монет',
        default=0
    )
    profile_photo = models.ImageField(
        'Фото профиля',
        default='user.png', upload_to='profile_photos'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def token(self):
        token, created = Token.objects.get_or_create(user=self)
        return token.key

    def status(self):
        if 100 <= self.coins < 500:
            return "Стандарт"
        elif 500 <= self.coins < 1000:
            return "Бронза"
        elif 1000 <= self.coins < 5000:
            return "Серебро"
        elif self.coins >= 5000:
            return "Золото"
        else:
            return "No Status"


class Payments(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Пользователь'
    )
    coins = models.FloatField(
        'Количество монет'
    )
    created_at = models.DateTimeField(
        'Дата операции',
        auto_now_add=True
    )
    info = models.CharField(
        max_length=255
    )

    def __str__(self):
        return f"Платеж {self.datetime}"

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


class BuyAsmanRequest(models.Model):
    STATUS_CHOICES = (
        (1, 'Подтвержденно'),
        (0, 'Отклоненно'),
    )

    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Пользователь')
    screenshot = models.ImageField(
        'Скриншот транзакции', upload_to='buy_asman'
    )
    status = models.IntegerField(
        'Статус', choices=STATUS_CHOICES, default=1
    )
    created_at = models.DateTimeField(
        'Дата операции', auto_now_add=True
    )
    processed = models.BooleanField(
        'Обработано', default=False
    )

    def __str__(self):
        return f"Покупка от {self.user.email}"

    class Meta:
        verbose_name = 'Покупка Asman'
        verbose_name_plural = 'Покупки Asman'
