import uuid
from django.db import models
from django.utils import timezone

from src.accounts.models import User
from src.discount.models import Partner


class AsmanRate(models.Model):
    rate = models.FloatField('Курс')
    standard = models.FloatField('Стандарт')
    bronze = models.FloatField('Бронза')
    silver = models.FloatField('Серебро')
    gold = models.FloatField('Золото')
    vip = models.FloatField('VIP')

    def __str__(self):
        return 'Курс Asman и Статусы'

    class Meta:
        verbose_name = 'Asman (курс и статус)'
        verbose_name_plural = 'Asman (курс и статус)'


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
    processed = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"Покупка от {self.user.email}"

    class Meta:
        verbose_name = 'Покупка Asman'
        verbose_name_plural = 'Asman (покупки)'
        ordering = ('-operation_time',)

    def confirm_purchase(self):
        if self.processed:
            return False
        if self.status == 1 and self.amount:
            self.user.balance += self.amount
            self.user.save()
            return True
        if self.status == 0:
            return True

    def save(self, *args, **kwargs):
        if self.confirm_purchase():
            self.processed = True
        super().save(*args, **kwargs)


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
        verbose_name_plural = 'Asman (выводы)'
        ordering = ('-operation_time',)


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
        ordering = ('-operation_time',)


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
        ordering = ('-operation_time',)


class History(models.Model):
    STATUS_CHOICES = (
        (1, 'Успешно'),
        (0, 'Ошибка'),
        (2, 'В обработке')
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        max_length=36
    )
    user = models.ForeignKey(
        User,
        verbose_name='Плательщик',
        on_delete=models.DO_NOTHING,
        related_name='user1'
    )
    recipient = models.ForeignKey(
        User,
        verbose_name='Получатель',
        on_delete=models.DO_NOTHING,
        null=True, blank=True,
        related_name='user2'
    )
    partner = models.ForeignKey(
        Partner,
        verbose_name='Партнер',
        on_delete=models.DO_NOTHING,
        null=True, blank=True
    )
    info = models.CharField(
        'Тип платежа',
        max_length=255
    )
    total = models.FloatField('Сумма')
    operation_time = models.DateTimeField(
        'Дата операции',
        default=timezone.now,
    )
    status = models.IntegerField(
        'Статус',
        choices=STATUS_CHOICES,
        default=2
    )

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'История платежей'
        ordering = ('-operation_time',)
