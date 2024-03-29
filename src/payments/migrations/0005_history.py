# Generated by Django 4.2.11 on 2024-03-19 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0004_asmanrate_vip'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('info', models.CharField(max_length=255, verbose_name='Тип платежа')),
                ('total', models.FloatField(verbose_name='Сумма')),
                ('operation_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата операции')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Плательщик')),
            ],
        ),
    ]
