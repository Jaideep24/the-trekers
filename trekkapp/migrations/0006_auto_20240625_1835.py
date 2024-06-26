# Generated by Django 3.2.25 on 2024-06-25 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trekkapp', '0005_auto_20240624_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='date',
            field=models.DateField(default=datetime.date(2024, 6, 25)),
        ),
        migrations.AlterField(
            model_name='city',
            name='inclusions',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='city',
            name='info',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='city',
            name='itenary',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
