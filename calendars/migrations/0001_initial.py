# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 12:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organisation', '0009_companydescription_service_hours'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('busy', models.BooleanField(default=False)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organisation.Company')),
            ],
            options={
                'ordering': ('start', 'end'),
                'verbose_name': 'calendar entry',
                'verbose_name_plural': 'calendar entries',
            },
        ),
    ]
