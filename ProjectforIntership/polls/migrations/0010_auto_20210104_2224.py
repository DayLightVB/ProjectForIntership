# Generated by Django 3.1.1 on 2021-01-04 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20210104_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='product_type',
            field=models.CharField(max_length=35, verbose_name='Type'),
        ),
    ]
