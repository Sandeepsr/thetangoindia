# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-13 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_fbevents_location_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbevents',
            name='Location_Name',
            field=models.CharField(default='Check Facebook Link for details', max_length=500),
        ),
    ]
