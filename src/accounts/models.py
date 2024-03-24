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
    referred_by = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True, blank=True
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


class UserStatuses(models.Model):
    standard = models.FloatField('Стандарт')
    bronze = models.FloatField('Бронза')
    silver = models.FloatField('Серебро')
    gold = models.FloatField('Золото')
    vip = models.FloatField('VIP')

    def __str__(self):
        return 'Статус'

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
