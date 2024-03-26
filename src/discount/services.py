import os
import qrcode
from django.utils import timezone
from django.conf import settings
from src.payments.models import Payment


def generate_partner_qrcode(instance):
    qr = qrcode.make(f'{instance.id}?type=2', border=2)
    qr_path = f"partner_qrcodes/{instance.id}.png"
    qr.save(os.path.join(settings.MEDIA_ROOT, qr_path))
    instance.qr.name = qr_path
    instance.save()

    return instance


def get_last_payment(partner, user):
    last_payment = Payment.objects.filter(partner=partner, user=user)

    if not last_payment.exists():
        return True

    return (timezone.now() - last_payment.order_by('-operation_time').first().operation_time).days
