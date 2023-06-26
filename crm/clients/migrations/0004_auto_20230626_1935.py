# Generated by Django 3.2.19 on 2023-06-26 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('clients', '0003_auto_20230625_2108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientanalytics',
            options={'verbose_name': 'Аналитика клиента', 'verbose_name_plural': 'Аналитика клиентов'},
        ),
        migrations.AlterModelOptions(
            name='clientstatistics',
            options={'verbose_name': 'Статистика клиента', 'verbose_name_plural': 'Статистика клиентов'},
        ),
        migrations.AlterField(
            model_name='clientanalytics',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='analytics', to='clients.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='clientstatistics',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='statistics', to='clients.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='clientstatistics',
            name='first_completed_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_statistics', to='orders.order', verbose_name='Первый выполненный заказ'),
        ),
        migrations.AlterField(
            model_name='clientstatistics',
            name='last_completed_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_statistics', to='orders.order', verbose_name='Последний выполненный заказ'),
        ),
    ]
