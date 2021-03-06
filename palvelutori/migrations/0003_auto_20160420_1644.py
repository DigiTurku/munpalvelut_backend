# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-20 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0005_company_service_areas'),
        ('palvelutori', '0002_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organisation.Company'),
        ),
        migrations.AddField(
            model_name='user',
            name='company_role',
            field=models.CharField(blank=True, help_text="User's role in the company", max_length=128),
        ),
        migrations.AddField(
            model_name='user',
            name='vetuma',
            field=models.CharField(blank=True, help_text='Vetuma identification code', max_length=128),
        ),
    ]
