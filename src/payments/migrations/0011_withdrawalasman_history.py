# Generated by Django 4.2.11 on 2024-03-21 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0010_withdrawalasman_address_alter_buyasman_history_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawalasman',
            name='history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payments.history', verbose_name='Покупка Asman'),
        ),
    ]
