# Generated by Django 3.2.19 on 2023-06-12 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_date_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='dispatcher',
            new_name='created_by',
        ),
    ]
