from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (
    Transfer,
    Payment
)
from .services import (
    make_transfer,
    make_payment
)


@receiver(post_save, sender=Transfer)
def make_transfer_on_save(sender, instance, created, **kwargs):
    if created:
        make_transfer(instance)


@receiver(post_save, sender=Payment)
def make_payment_on_save(sender, instance, created, **kwargs):
    if created:
        make_payment(instance)
