# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-14 20:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0010_auto_20181014_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionalprofile',
            name='phone_number',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]