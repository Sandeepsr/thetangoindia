# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-13 07:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_auto_20161113_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fbevents',
            name='Location_Name',
        ),
    ]
