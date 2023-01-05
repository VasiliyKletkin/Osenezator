# Generated by Django 4.1.4 on 2023-01-05 14:34

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=255, verbose_name='Address line 1')),
                ('address2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address line 2')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('volume', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Volume')),
                ('description', models.TextField(blank=True, max_length=255, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Last Name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('is_active', models.BooleanField(default=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='clients.address')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='companies.company')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
