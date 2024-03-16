from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (
    User,
)
from .services import (
    generate_user_qrcode,
)


@receiver(post_save, sender=User)
def generate_qrcode_on_save(sender, instance, created, **kwargs):
    if created:
        generate_user_qrcode(instance)
