# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-04 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_guestemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_pro',
            field=models.BooleanField(default=False),
        ),
    ]
