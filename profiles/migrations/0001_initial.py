# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-07 17:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authtools', '0003_auto_20160128_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='FBEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Attending_Count', models.IntegerField(default=0)),
                ('Cover', models.URLField(blank=True, null=True)),
                ('Event_Name', models.CharField(blank=True, max_length=928, null=True)),
                ('Event_Link', models.URLField(blank=True, null=True)),
                ('Start_Time', models.DateTimeField()),
                ('Event_Id', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=99998, null=True)),
                ('End_Time', models.DateTimeField()),
                ('Place', models.CharField(blank=True, max_length=9999, null=True)),
                ('Updated_Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='FBLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.IntegerField(unique=True)),
                ('Group_Url', models.URLField(null=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('slug', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y-%m-%d/', verbose_name='Profile picture')),
                ('bio', models.CharField(blank=True, max_length=200, null=True, verbose_name='Short Bio')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email verified')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tango_Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=928, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('updated_time', models.DateTimeField()),
                ('post_type', models.CharField(blank=True, max_length=128, null=True)),
                ('post_name', models.CharField(blank=True, max_length=998, null=True)),
                ('permalink_url', models.URLField(blank=True)),
                ('picture', models.URLField(blank=True, null=True)),
                ('post_id', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=9998, null=True)),
                ('post_from', models.CharField(blank=True, max_length=998)),
                ('created_time', models.DateTimeField()),
                ('place', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tango_Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('group_url', models.URLField(null=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='TangoCommunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TangoCommunityInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=928, null=True)),
                ('description', models.CharField(blank=True, max_length=4928, null=True)),
                ('class_location', models.CharField(blank=True, max_length=928, null=True)),
                ('class_timings', models.CharField(blank=True, max_length=928, null=True)),
                ('class_location1', models.CharField(blank=True, max_length=928, null=True)),
                ('class_timings1', models.CharField(blank=True, max_length=928, null=True)),
                ('class_location2', models.CharField(blank=True, max_length=928, null=True)),
                ('class_timings2', models.CharField(blank=True, max_length=928, null=True)),
                ('class_location3', models.CharField(blank=True, max_length=928, null=True)),
                ('class_timings3', models.CharField(blank=True, max_length=928, null=True)),
                ('class_location_map', models.URLField(blank=True)),
                ('class_location_map1', models.URLField(blank=True)),
                ('instructor_name', models.CharField(blank=True, max_length=928, null=True)),
                ('fees', models.CharField(blank=True, max_length=928, null=True)),
                ('admission_process', models.CharField(blank=True, max_length=5928, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('email1', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=928, null=True)),
                ('fb_url', models.URLField(blank=True)),
                ('fb_url1', models.URLField(blank=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('website1', models.URLField(blank=True, null=True)),
                ('milonga_venue', models.CharField(blank=True, max_length=4928, null=True)),
                ('milonga_venue_map_link', models.URLField(blank=True)),
                ('milonga_time', models.CharField(blank=True, max_length=928, null=True)),
                ('practica_venue', models.CharField(blank=True, max_length=4928, null=True)),
                ('practica_venue_map_link', models.URLField(blank=True)),
                ('practica_time', models.CharField(blank=True, max_length=928, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.TangoCommunity')),
            ],
        ),
        migrations.AddField(
            model_name='tango_events',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Tango_Location'),
        ),
        migrations.AddField(
            model_name='fbevents',
            name='Location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.FBLocation'),
        ),
    ]
