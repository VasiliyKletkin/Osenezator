# Generated by Django 4.1.4 on 2023-06-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0004_alter_district_city'),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='districts',
            field=models.ManyToManyField(related_name='companies', to='addresses.district', verbose_name='Районы которых принимаются заказы'),
        ),
        migrations.AddField(
            model_name='company',
            name='regions',
            field=models.ManyToManyField(related_name='companies', to='addresses.region', verbose_name='Регионы из которых принимаются заказы'),
        ),
        migrations.RemoveField(
            model_name='company',
            name='country',
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.ManyToManyField(related_name='companies', to='addresses.country', verbose_name='Страны из которых принимаются заказы'),
        ),
    ]
