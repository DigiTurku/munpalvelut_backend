# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0012_auto_20160511_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='psop',
            field=models.BooleanField(default=False, help_text='Palveluseteli ja ostopalvelutuottaja'),
        ),
        migrations.AlterField(
            model_name='companydescription',
            name='service_hours',
            field=models.CharField(blank=True, help_text='Freeform service description of service hours.', max_length=255),
        ),
        migrations.AlterField(
            model_name='companydescription',
            name='shorttext',
            field=models.TextField(blank=True, help_text='Short, (a sentence or two) description of the company.'),
        ),
        migrations.AlterField(
            model_name='companydescription',
            name='text',
            field=models.TextField(blank=True, help_text='Full description'),
        ),
    ]
