# Generated by Django 4.1.4 on 2023-07-06 17:08

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispatcher',
            fields=[
            ],
            options={
                'verbose_name': 'Диспетчера',
                'verbose_name_plural': 'Диспетчеры',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
            ],
            options={
                'verbose_name': 'Водителя',
                'verbose_name_plural': 'Водители',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
            ],
            options={
                'verbose_name': 'Владельца',
                'verbose_name_plural': 'Владельцы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('number', models.CharField(max_length=255, verbose_name='Регистрационный номер')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='companies.company', verbose_name='Компания')),
                ('driver', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='car', to=settings.AUTH_USER_MODEL, verbose_name='Водитель')),
            ],
            options={
                'verbose_name': 'Машину',
                'verbose_name_plural': 'Машины',
            },
        ),
    ]
