# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-01 03:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerprofile',
            name='email',
        ),
    ]