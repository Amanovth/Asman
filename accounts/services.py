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
