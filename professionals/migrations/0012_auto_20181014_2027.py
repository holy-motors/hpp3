# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-14 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0011_auto_20181014_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionalprofile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]