# Generated by Django 4.2.11 on 2024-03-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='qr',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='QR'),
        ),
    ]
