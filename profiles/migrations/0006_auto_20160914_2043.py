# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-14 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20160914_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbevents',
            name='Event_Id',
            field=models.CharField(default='0', max_length=200, unique=True),
        ),
    ]
