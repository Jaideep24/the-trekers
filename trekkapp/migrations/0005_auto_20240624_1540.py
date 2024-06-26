# Generated by Django 3.2.25 on 2024-06-24 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trekkapp', '0004_auto_20240621_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='camping',
            name='upcoming',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='city',
            name='upcoming',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cycling',
            name='upcoming',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tours',
            name='upcoming',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='city',
            name='date',
            field=models.DateField(default=datetime.date(2024, 6, 24)),
        ),
    ]
