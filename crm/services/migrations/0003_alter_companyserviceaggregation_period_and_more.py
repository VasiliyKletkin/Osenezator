# Generated by Django 4.1.4 on 2023-07-06 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_companyserviceaggregation_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyserviceaggregation',
            name='period',
            field=models.CharField(choices=[('30', '1 Месяц'), ('90', '3 Месяца'), ('180', '6 Месяцев'), ('360', '12 Месяцев')], default='30', max_length=50, verbose_name='Период'),
        ),
        migrations.AlterField(
            model_name='companyservicecrm',
            name='period',
            field=models.CharField(choices=[('30', '1 Месяц'), ('90', '3 Месяца'), ('180', '6 Месяцев'), ('360', '12 Месяцев')], default='30', max_length=50, verbose_name='Период'),
        ),
    ]