# Generated by Django 4.1.4 on 2023-07-07 09:21

from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('companies', '0001_initial'),
        ('employees', '0001_initial'),
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', model_utils.fields.StatusField(choices=[('CONFIRMATION', 'Подтверждение'), ('CONFIRMED', 'Подтвержден'), ('INPROGRESS', 'Выполняется'), ('COMPLETED', 'Выполнен'), ('CANCELED', 'Отменен')], default='CONFIRMED', max_length=100, no_check_for_status=True, verbose_name='Статус')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('type_payment', models.CharField(choices=[('CASH', 'Наличные'), ('CREDIT_CARD', 'Картой'), ('ONLINE_TRANSFER', 'Онлайн перевод')], default='ONLINE_TRANSFER', max_length=20, verbose_name='Тип оплаты')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_planned', models.DateTimeField(blank=True, null=True, verbose_name='Планируемая дата выполнения')),
                ('date_started', model_utils.fields.MonitorField(blank=True, default=None, monitor='status', null=True, verbose_name='Дата начала выполнения', when={'INPROGRESS'})),
                ('date_completed', model_utils.fields.MonitorField(blank=True, default=None, monitor='status', null=True, verbose_name='Дата конца выполнения', when={'COMPLETED'})),
                ('date_canceled', model_utils.fields.MonitorField(blank=True, default=None, monitor='status', null=True, verbose_name='Дата отмены выполнения', when={'CANCELED'})),
                ('is_sent', models.BooleanField(default=False, verbose_name='Отправлен водителю')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='addresses.address', verbose_name='Адрес')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='clients.client', verbose_name='Клиент')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='companies.company', verbose_name='Компания')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_orders', to='employees.dispatcher', verbose_name='Диспетчер')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='employees.driver', verbose_name='Водитель')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['status'], name='order_status_idx'),
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['date_created'], name='order_date_created_idx'),
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['is_sent'], name='order_is_sent_idx'),
        ),
    ]
