# Generated by Django 4.2.11 on 2024-03-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_address_asman_wallets_asman_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsmanRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(verbose_name='Курс')),
            ],
        ),
    ]
