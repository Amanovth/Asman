from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Partners
from .services import generate_partner_qrcode


@receiver(post_save, sender=Partners)
def generate_qrcode_on_save(sender, instance, created, **kwargs):
    if created:
        generate_partner_qrcode(instance)
