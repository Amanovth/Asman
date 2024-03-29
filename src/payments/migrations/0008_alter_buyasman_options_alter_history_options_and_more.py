# Generated by Django 4.2.11 on 2024-03-21 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_alter_payment_options_alter_history_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyasman',
            options={'ordering': ('-operation_time',), 'verbose_name': 'Покупка Asman', 'verbose_name_plural': 'Asman (покупки)'},
        ),
        migrations.AlterModelOptions(
            name='history',
            options={'ordering': ('-operation_time',), 'verbose_name': 'Платеж', 'verbose_name_plural': 'История платежей'},
        ),
        migrations.AlterModelOptions(
            name='transfer',
            options={'ordering': ('-operation_time',), 'verbose_name': 'Перевод', 'verbose_name_plural': 'Переводы'},
        ),
        migrations.AlterModelOptions(
            name='withdrawalasman',
            options={'ordering': ('-operation_time',), 'verbose_name': 'Вывод Asman', 'verbose_name_plural': 'Asman (выводы)'},
        ),
        migrations.AddField(
            model_name='history',
            name='buy_asman',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='payments.buyasman', verbose_name='Покупка Asman'),
        ),
    ]
