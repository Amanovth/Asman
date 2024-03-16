from django.db import models
from django.utils import timezone

from src.accounts.models import User
from src.discount.models import Partner


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
