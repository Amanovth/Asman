import os
import string
import random
import qrcode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_verification_mail(instance):
    to_email = instance.get('email')
    subject = 'Подтвердите адрес электронной почты'

    message = render_to_string('index.html', {'instance': instance})

    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [to_email])
    email.content_subtype = "html"
    email.send()


def generate_password(length=8):
    characters = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def forgot_password(email, password):
    subject = 'Ваш новый пароль'

    message = render_to_string('forgot_password.html', {'password': password})

    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
    email.content_subtype = "html"
    email.send()


def generate_user_qrcode(instance):
    qr = qrcode.make(f'{instance.id}?type=1', border=2)
    qr_path = f"user_qrcodes/{instance.id}.png"
    qr.save(os.path.join(settings.MEDIA_ROOT, qr_path))
    instance.qr.name = qr_path
    instance.save()

    return instance


def calculate_user_status(user_rate, asman_rate):
    if user_rate >= asman_rate.vip:
        return 'VIP'
    if user_rate >= asman_rate.gold:
        return 'Золото'
    elif user_rate >= asman_rate.silver:
        return 'Серебро'
    elif user_rate >= asman_rate.bronze:
        return 'Бронза'
    elif user_rate >= asman_rate.standard:
        return 'Стандарт'
    else:
        return 'Unknown'

