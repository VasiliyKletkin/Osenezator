# Generated by Django 4.1.4 on 2023-06-01 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_remove_street_city_street_district_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='street',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='streets', to='addresses.district', verbose_name='Район'),
        ),
    ]
