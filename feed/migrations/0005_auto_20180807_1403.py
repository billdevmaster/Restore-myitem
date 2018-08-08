# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-07 08:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_claimform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=20)),
                ('Description', models.TextField()),
                ('image', models.FileField(upload_to='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AlterField(
            model_name='report_item',
            name='Description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='report_item',
            name='item_name',
            field=models.CharField(max_length=60),
        ),
    ]