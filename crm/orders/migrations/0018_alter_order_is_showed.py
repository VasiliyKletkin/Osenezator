# Generated by Django 4.1.4 on 2023-03-17 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_rename_is_sent_order_is_showed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_showed',
            field=models.BooleanField(default=False, verbose_name='Отправлен водителю'),
        ),
    ]
