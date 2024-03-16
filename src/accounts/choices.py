from django.db import models
from django.utils.translation import gettext_lazy as _


class UserStatus(models.TextChoices):
    STANDART = 'standart', _('Стандарт')
    BRONZE = 'bronze', _('Бронза')
    SILVER = 'silver', _('Серебро')
    GOLD = 'gold', _('Золото')
