from django.db import models

from django.db import models
from django.utils.translation import gettext_lazy as _


class Stories(models.Model):
    created_at = models.DateTimeField(_("Дата и время"), auto_now_add=True)
    img = models.ImageField(_("Изображение"), upload_to="story_images", null=True, blank=True)

    class Meta:
        verbose_name = _("История")
        verbose_name_plural = _("Истории")


class StoryVideos(models.Model):
    story = models.ForeignKey(Stories, on_delete=models.CASCADE, related_name="stories")
    url = models.FileField(_("История"), upload_to="stories")
    created_at = models.DateTimeField(_("Дата и время"), auto_now_add=True)

    class Meta:
        verbose_name = _("История")
        verbose_name_plural = _("Истории")

    def __str__(self) -> str:
        return self.created_at.strftime("%d %B %Y г. %H:%M")


class Wallets(models.Model):
    asman = models.CharField(
        'Asman',
        max_length=255
    )
    usdt = models.CharField(
        'USDT',
        max_length=255
    )

    def __str__(self):
        return 'Кошелек'

    class Meta:
        verbose_name = 'Кошелек'
        verbose_name_plural = 'Кошельки'


class AsmanRate(models.Model):
    rate = models.FloatField(
        'Курс'
    )

    class Meta:
        verbose_name = 'Курс Asman'
        verbose_name_plural = 'Курс Asman'
