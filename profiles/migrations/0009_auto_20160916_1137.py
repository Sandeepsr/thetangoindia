# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-16 06:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20160916_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tango_events',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.Tango_Location'),
        ),
    ]
