# Generated by Django 3.2.25 on 2024-06-19 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trekkapp', '0002_auto_20240619_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='date',
            field=models.DateField(default=datetime.date(2024, 6, 19)),
        ),
        migrations.AddField(
            model_name='city',
            name='difficulty',
            field=models.CharField(default='easy', max_length=100),
        ),
        migrations.AddField(
            model_name='city',
            name='fees',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='inclusions',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='city',
            name='info',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='city',
            name='intro',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='city',
            name='itenary',
            field=models.CharField(default='', max_length=100),
        ),
    ]
