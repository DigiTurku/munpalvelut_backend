# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-19 13:41
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0004_auto_20160419_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='service_areas',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5), default=[], help_text='Postal codes of the areas in which this company provides service', size=None),
            preserve_default=False,
        ),
    ]
