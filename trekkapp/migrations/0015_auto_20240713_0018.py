# Generated by Django 3.2.25 on 2024-07-12 18:48

import datetime
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('trekkapp', '0014_auto_20240711_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', tinymce.models.HTMLField()),
                ('date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(default='default-ui-image-placeholder-wireframes-600nw-1037719192 (1).png', upload_to='')),
                ('likes', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='camping',
            name='date',
            field=models.DateField(default=datetime.date(2024, 7, 12)),
        ),
        migrations.AlterField(
            model_name='city',
            name='date',
            field=models.DateField(default=datetime.date(2024, 7, 12)),
        ),
        migrations.AlterField(
            model_name='cycling',
            name='date',
            field=models.DateField(default=datetime.date(2024, 7, 12)),
        ),
        migrations.AlterField(
            model_name='tours',
            name='date',
            field=models.DateField(default=datetime.date(2024, 7, 12)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default=' ')),
                ('comment', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trekkapp.article')),
            ],
        ),
    ]
