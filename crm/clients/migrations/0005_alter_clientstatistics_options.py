# Generated by Django 3.2.19 on 2023-06-24 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_rename_date_order_planned_clientstatistics_date_planned_next_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientstatistics',
            options={'verbose_name': 'Статистика o клиенте', 'verbose_name_plural': 'Статистика o клиенте'},
        ),
    ]
