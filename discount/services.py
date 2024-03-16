import os
import qrcode
from django.conf import settings


def generate_partner_qrcode(instance):
    qr = qrcode.make(str(instance.id), border=2)
    qr_path = f"partner_qrcodes/{instance.id}.png"
    qr.save(os.path.join(settings.MEDIA_ROOT, qr_path))
    instance.qr.name = qr_path
    instance.save()

    return instance
