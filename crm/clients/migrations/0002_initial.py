# Generated by Django 3.2.19 on 2023-06-26 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('companies', '0001_initial'),
        ('clients', '0001_initial'),
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientstatistics',
            name='first_completed_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_statistics', to='orders.order', verbose_name='Первый выполненный заказ'),
        ),
        migrations.AddField(
            model_name='clientstatistics',
            name='last_completed_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_statistics', to='orders.order', verbose_name='Последний выполненный заказ'),
        ),
        migrations.AddField(
            model_name='clientanalytics',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='analytics', to='clients.client', verbose_name='Клиент'),
        ),
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clients', to='addresses.address', verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='client',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='clients', to='companies.company', verbose_name='Компания'),
        ),
        migrations.CreateModel(
            name='ClientBilling',
            fields=[
            ],
            options={
                'verbose_name': 'Биллинг Клиента',
                'verbose_name_plural': 'Биллинг Клиентов',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('clients.client',),
        ),
    ]