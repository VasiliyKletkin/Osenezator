# Generated by Django 3.2.19 on 2023-06-24 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_clientstatistics_date_order_planned'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientstatistics',
            old_name='date_order_planned',
            new_name='date_planned_next_order',
        ),
    ]
