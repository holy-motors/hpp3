# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-14 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0008_auto_20181014_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionalprofile',
            name='speciality',
            field=models.CharField(choices=[('dental', 'Dental'), ('vision', 'Vision'), ('physical', 'Physical'), ('psychological', 'Psychological')], default='dental', max_length=120),
        ),
    ]
