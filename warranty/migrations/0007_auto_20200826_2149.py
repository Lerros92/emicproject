# Generated by Django 3.1 on 2020-08-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warranty', '0006_auto_20200826_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='numExport',
            field=models.CharField(blank=True, max_length=10, verbose_name='Số phiếu xuất'),
        ),
    ]
