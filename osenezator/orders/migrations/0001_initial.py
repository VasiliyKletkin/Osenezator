# Generated by Django 4.1.4 on 2023-01-05 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        ('drivers', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Price')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_complited', models.DateTimeField(auto_now_add=True, verbose_name='Date complited')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('status', models.CharField(choices=[('CONFIRMATION', 'Confirmation'), ('INPROGRESS', 'Inprogress'), ('COMPLETED', 'Completed'), ('CANCELED', 'Canceled')], default='CONFIRMATION', max_length=20, verbose_name='Status')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='clients.client')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='companies.company')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='drivers.driver')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
