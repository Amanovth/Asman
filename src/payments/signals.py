from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (
    Transfer,
    Payment,
    History,
    BuyAsman
)
from .services import (
    make_transfer,
    make_payment
)


@receiver(post_save, sender=BuyAsman)
def create_history(sender, instance, created, **kwargs):
    if created:
        History.objects.create(
            user=instance.user,
            status=1
        )
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
