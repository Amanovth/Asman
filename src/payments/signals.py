from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (
    Transfer,
    Payment,
    History,
    BuyAsman,
    WithdrawalAsman
)
from .services import (
    make_transfer,
    make_payment
)


@receiver(post_save, sender=BuyAsman)
def create_history_when_buying_asman(sender, instance, created, **kwargs):
    if created:
        obj = History.objects.create(
            user=instance.user,
            status=instance.status,
            info='Покупка Asman',
            total=0,
            operation_time=instance.operation_time
        )
        instance.history = obj
        instance.save()


@receiver(post_save, sender=WithdrawalAsman)
def create_history_when_withdrawing_asman(sender, instance, created, **kwargs):
    if created:
        obj = History.objects.create(
            user=instance.user,
            status=instance.status,
            info='Вывод Asman',
            total=instance.amount,
            operation_time=instance.operation_time
        )
        instance.history = obj
        instance.save()


@receiver(post_save, sender=Transfer)
def make_transfer_on_save(sender, instance, created, **kwargs):
    if created:
        History.objects.create(
            user=instance.payer,
            recipient=instance.recipient,
            status=1,
            info="Перевод",
            total=instance.amount,
            operation_time=instance.operation_time
        )
        make_transfer(instance)


@receiver(post_save, sender=Payment)
def make_payment_on_save(sender, instance, created, **kwargs):
    if created:
        History.objects.create(
            user=instance.user,
            partner=instance.partner,
            status=1,
            info="Покупка услуг",
            total=instance.partner.cost_of_visit,
            operation_time=instance.operation_time
        )
        make_payment(instance)
