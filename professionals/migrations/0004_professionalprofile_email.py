# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-14 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0003_auto_20181014_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='professionalprofile',
            name='email',
            field=models.EmailField(default='healplan@plus.com', max_length=255),
        ),
    ]
