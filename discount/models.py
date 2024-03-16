from django.db import models
from ckeditor.fields import RichTextField


class PartnerCategory(models.Model):
    name = models.CharField(
        'Название',
        max_length=255
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория партнера'
        verbose_name_plural = 'Категории партнеров'


class Partners(models.Model):
    cat = models.ForeignKey(
        PartnerCategory,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        related_name='partners'
    )
    title = models.CharField(
        'Заголовок',
        max_length=255
    )
    description = RichTextField(
        'Описание',
    )
    qr = models.ImageField(
        'QR',
        null=True,
        blank=True,
        editable=False,
    )
    img = models.ImageField(
        'Изображение',
        upload_to='partners'
    )
    total_visits = models.IntegerField(
        'Всего посещений',
        default=0
    )
    cost_of_visit = models.FloatField(
        'Стоимость посещения'
    )
    is_active = models.BooleanField(
        'Is active',
        default=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
