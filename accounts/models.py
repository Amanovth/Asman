import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token

from discount.models import Partner
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
    balance = models.FloatField(
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


class BuyAsman(models.Model):
    STATUS_CHOICES = (
        (1, 'Подтверждено'),
        (0, 'Отклонено'),
        (2, '')
    )

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='Пользователь'
    )
    amount = models.FloatField(
        'Сумма',
        null=True,
        blank=True
    )
    img = models.ImageField(
        'Скриншот транзакции',
        upload_to='buy_asman'
    )
    status = models.IntegerField(
        'Статус',
        choices=STATUS_CHOICES,
        default=2
    )
    operation_time = models.DateTimeField(
        'Дата операции',
        default=timezone.now
    )

    def __str__(self):
        return f"Покупка от {self.user.email}"

    class Meta:
        verbose_name = 'Покупка Asman'
        verbose_name_plural = 'Покупки Asman'


class WithdrawalAsman(models.Model):
    STATUS_CHOICES = (
        (1, 'Подтверждено'),
        (0, 'Отклонено'),
        (2, '')
    )

    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.DO_NOTHING
    )
    amount = models.FloatField(
        'Сумма',
    )
    status = models.IntegerField(
        'Статус',
        choices=STATUS_CHOICES,
        default=2
    )
    operation_time = models.DateTimeField(
        'Дата операции',
        default=timezone.now
    )

    def __str__(self):
        return f"Вывод от {self.user.email}"

    class Meta:
        verbose_name = 'Вывод Asman'
        verbose_name_plural = 'Выводы Asman'


class Payment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Пользователь'
    )
    partner = models.ForeignKey(
        Partner,
        verbose_name='Партнер',
        on_delete=models.DO_NOTHING
    )
    operation_time = models.DateTimeField(
        'Дата операции',
        default=timezone.now
    )

    def __str__(self):
        return f"Платеж {self.operation_time}"

    class Meta:
        verbose_name = 'Покупка услуги'
        verbose_name_plural = 'Покупки услуг'


class Transfer(models.Model):
    payer = models.ForeignKey(
        User,
        verbose_name='Плательщик',
        on_delete=models.DO_NOTHING,
        related_name='payer',
    )
    recipient = models.ForeignKey(
        User,
        verbose_name='Получатель',
        on_delete=models.DO_NOTHING,
        related_name='recipient'
    )
    amount = models.FloatField(
        'Сумма',
    )
    operation_time = models.DateTimeField(
        'Дата операции',
        default=timezone.now,
    )

    def __str__(self):
        return f"{self.payer.email} > {self.recipient.email}"

    class Meta:
        verbose_name = 'Перевод'
        verbose_name_plural = 'Переводы'
