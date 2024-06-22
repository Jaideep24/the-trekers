# Generated by Django 3.2.25 on 2024-06-21 11:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trekkapp', '0003_auto_20240619_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='adventure',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='trekkapp.adventure'),
        ),
        migrations.AlterField(
            model_name='city',
            name='date',
            field=models.DateField(default=datetime.date(2024, 6, 21)),
        ),
        migrations.AlterField(
            model_name='city',
            name='festival',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='trekkapp.festival'),
        ),
        migrations.AlterField(
            model_name='city',
            name='trekking',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='trekkapp.trekking'),
        ),
    ]
