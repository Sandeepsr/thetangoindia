# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-11 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20160908_1521'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fbevents',
            options={},
        ),
        migrations.AlterField(
            model_name='fbevents',
            name='Event_Id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
