# Generated by Django 3.2.25 on 2024-07-09 08:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trekkapp', '0009_auto_20240708_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camping',
            name='date',
            field=models.DateField(default=datetime.date(2024, 7, 9)),
        ),
        migrations.AlterField(
            model_name='city',
            name='date',
            field=models.DateField(default=datetime.date(2024, 7, 9)),
        ),
        migrations.AlterField(
            model_name='cycling',
            name='date',
            field=models.DateField(default=datetime.date(2024, 7, 9)),
        ),
        migrations.AlterField(
            model_name='tours',
            name='date',
            field=models.DateField(default=datetime.date(2024, 7, 9)),
        ),
        
    ]
