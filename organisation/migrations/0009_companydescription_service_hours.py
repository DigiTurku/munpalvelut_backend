# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0008_company_price_per_hour_continuing'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydescription',
            name='service_hours',
            field=models.CharField(default='', help_text='Freeform service description of service hours.', max_length=255),
            preserve_default=False,
        ),
    ]