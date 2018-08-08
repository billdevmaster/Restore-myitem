# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_auto_20180809_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_item',
            name='city',
            field=models.CharField(help_text='*Enter the city name', max_length=60),
        ),
        migrations.AlterField(
            model_name='report_item',
            name='title',
            field=models.CharField(help_text='*Enter the item name you found e.g. Marksheet,key,wallet', max_length=255),
        ),
    ]
