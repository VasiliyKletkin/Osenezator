# Generated by Django 3.2.19 on 2023-06-26 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
        ('companies', '0003_auto_20230626_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyworkplace',
            options={'verbose_name': 'Рабочее пространство для заказов', 'verbose_name_plural': 'Рабочее пространство для заказов'},
        ),
        migrations.AlterField(
            model_name='companyworkplace',
            name='cities',
            field=models.ManyToManyField(blank=True, related_name='work_places', to='addresses.City', verbose_name='Города или Населенные пункты из которых принимаются заказы'),
        ),
        migrations.AlterField(
            model_name='companyworkplace',
            name='company',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_place', to='companies.company'),
        ),
        migrations.AlterField(
            model_name='companyworkplace',
            name='countries',
            field=models.ManyToManyField(blank=True, related_name='work_places', to='addresses.Country', verbose_name='Страны из которых принимаются заказы'),
        ),
        migrations.AlterField(
            model_name='companyworkplace',
            name='regions',
            field=models.ManyToManyField(blank=True, related_name='work_places', to='addresses.Region', verbose_name='Регионы из которых принимаются заказы'),
        ),
        migrations.AlterField(
            model_name='companyworkplace',
            name='streets',
            field=models.ManyToManyField(blank=True, related_name='work_places', to='addresses.Street', verbose_name='Улицы из которых принимаются заказы'),
        ),
    ]
