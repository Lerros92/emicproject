# Generated by Django 3.1 on 2020-08-26 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warranty', '0005_auto_20200826_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='numExport',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Số phiếu xuất'),
        ),
    ]
