# Generated by Django 3.2.25 on 2024-07-11 08:03

import datetime
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('trekkapp', '0012_auto_20240710_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camping',
            name='date',
            field=models.DateField(default=datetime.date(2024, 7, 11)),
        ),
        migrations.AlterField(
            model_name='city',
            name='date',
            field=models.DateField(default=datetime.date(2024, 7, 11)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='cycling',
            name='date',
            field=models.DateField(default=datetime.date(2024, 7, 11)),
        ),
        migrations.AlterField(
            model_name='enquire',
            name='number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='personaltrek',
            name='number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='tours',
            name='date',
            field=models.DateField(default=datetime.date(2024, 7, 11)),
        ),
    ]
