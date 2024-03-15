# Generated by Django 4.2.11 on 2024-03-15 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_buyasmanrequest_screenshot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyasmanrequest',
            name='processed',
            field=models.BooleanField(default=False, verbose_name='Обработано'),
        ),
        migrations.AlterField(
            model_name='buyasmanrequest',
            name='status',
            field=models.IntegerField(choices=[(1, 'Подтвержденно'), (0, 'Отклоненно')], default=1, verbose_name='Статус'),
        ),
    ]
