# Generated by Django 3.2.19 on 2023-06-26 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home', models.CharField(max_length=255, verbose_name='Дом')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Страну',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='streets', to='addresses.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Улицу',
                'verbose_name_plural': 'Улицы',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='regions', to='addresses.country', verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
            },
        ),
        migrations.AddIndex(
            model_name='country',
            index=models.Index(fields=['name'], name='country_name_idx'),
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cities', to='addresses.region', verbose_name='Регион'),
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='addresses', to='addresses.street', verbose_name='Улица'),
        ),
        migrations.AddIndex(
            model_name='street',
            index=models.Index(fields=['name'], name='street_name_idx'),
        ),
        migrations.AddIndex(
            model_name='region',
            index=models.Index(fields=['name'], name='region_name_idx'),
        ),
        migrations.AddIndex(
            model_name='city',
            index=models.Index(fields=['name'], name='city_name_idx'),
        ),
        migrations.AddIndex(
            model_name='address',
            index=models.Index(fields=['home'], name='address_home_idx'),
        ),
    ]
