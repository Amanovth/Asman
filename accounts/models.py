from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    phone = models.CharField(_('Телефон'), max_length=255)
    email = models.EmailField(_('Email'), unique=True)
    v_code = models.CharField(_('Код подтверждения'), null=True, blank=True, max_length=6)
    verified = models.BooleanField(_('Подтверждено'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def token(self):
        token, created = Token.objects.get_or_create(user=self)
        return token.key

