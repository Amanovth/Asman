# Generated by Django 4.2.11 on 2024-03-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_asmanrate_alter_buyasman_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asmanrate',
            name='vip',
            field=models.FloatField(default=1, verbose_name='VIP'),
            preserve_default=False,
        ),
    ]
