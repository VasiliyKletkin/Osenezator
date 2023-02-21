# Generated by Django 4.1.4 on 2023-02-16 19:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_alter_order_date_planned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_planned',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Планируемая дата выполнения'),
        ),
    ]
