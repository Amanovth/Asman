# Generated by Django 4.2.11 on 2024-03-25 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0012_partner_visits_for_bronze_partner_visits_for_gold_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='visits_for_standard',
            field=models.IntegerField(blank=True, default=1, verbose_name='Посещения (Standard)'),
            preserve_default=False,
        ),
    ]
