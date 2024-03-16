from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.payments'
    verbose_name = 'Платежи'

    def ready(self):
        import src.payments.signals
