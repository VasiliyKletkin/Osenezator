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
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Car Name')),
                ('number', models.CharField(max_length=255, verbose_name='Car Number')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='companies.company')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('is_active', models.BooleanField(default=True)),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to='drivers.car')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drivers', to='companies.company')),
            ],
            options={
                'verbose_name': 'Driver',
                'verbose_name_plural': 'Drivers',
            },
        ),
    ]
