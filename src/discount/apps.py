from django.apps import AppConfig


class DiscountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.discount'
    verbose_name = 'Скидки'

    def ready(self):
        import src.discount.signals
