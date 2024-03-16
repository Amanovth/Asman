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


def get_payment_type(payment_type):
    payment_types = {
        1: 'Покупка Asman',
        2: 'Ввод Asman',
        3: 'Вывод Asman',
        4: 'Покупка услуги',
        5: 'Перевод между пользователями'
    }
    return payment_types.get(payment_type, 'Неизвестный тип платежа')


def make_transfer(instance):
    amount = instance.amount
    payer = instance.payer
    recipient = instance.recipient

    payer.balance -= amount
    recipient.balance += amount

    payer.save()
    recipient.save()

    return


def make_payment(instance):
    amount = instance.partner.cost_of_visit
    user = instance.user
    partner = instance.partner

    user.balance -= amount
    partner.total_visits += 1

    user.save()
    partner.save()

    return
