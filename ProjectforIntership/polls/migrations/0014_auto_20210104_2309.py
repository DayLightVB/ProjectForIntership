# Generated by Django 3.1.1 on 2021-01-04 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20210104_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='place',
            field=models.CharField(max_length=40, verbose_name='Place'),
        ),
    ]