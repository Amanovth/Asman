import uuid
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class PartnerCategory(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        max_length=36
    )
    name = models.CharField(
        'Название',
        max_length=255
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория партнера'
        verbose_name_plural = 'Категории партнеров'


class Partner(models.Model):
    is_active = models.BooleanField(
        'Активность',
        help_text='Отметьте, если партнер должен считаться активным. '
                  'Уберите эту отметку вместо удаления записи.',
        default=True
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        max_length=36
    )
    cost_of_visit = models.FloatField(
        'Стоимость посещения'
    )
    cat = models.ForeignKey(
        PartnerCategory,
        on_delete=models.CASCADE,
        verbose_name='Категория',
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
    date_joined = models.DateTimeField(
        'Дата регистрации',
        default=timezone.now
    )

    d_standard = models.IntegerField('Скидка (Standard)', blank=True)
    d_bronze = models.IntegerField('Скидка (Bronze)', blank=True)
    d_silver = models.IntegerField('Скидка (Silver)', blank=True)
    d_gold = models.IntegerField('Скидка (Gold)', blank=True)
    d_vip = models.IntegerField('Скидка (VIP)', blank=True)

    v_standard = models.IntegerField('Посещения (Standard)', blank=True)
    v_bronze = models.IntegerField('Посещения (Bronze)', blank=True)
    v_silver = models.IntegerField('Посещения (Silver)', blank=True)
    v_gold = models.IntegerField('Посещения (Gold)', blank=True)
    v_vip = models.IntegerField('Посещения (VIP)', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
