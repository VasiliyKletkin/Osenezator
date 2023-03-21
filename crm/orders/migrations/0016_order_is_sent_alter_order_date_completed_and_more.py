# Generated by Django 4.1.4 on 2023-03-15 13:46

from django.db import migrations, models
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_alter_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_sent',
            field=models.BooleanField(default=False, verbose_name='Отравленный'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_completed',
            field=model_utils.fields.MonitorField(blank=True, default=None, monitor='status', null=True, verbose_name='Дата завершения', when={'COMPLETED'}),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_started',
            field=model_utils.fields.MonitorField(blank=True, default=None, monitor='status', null=True, verbose_name='Дата начала выполнения', when={'INPROGRESS'}),
        ),
    ]