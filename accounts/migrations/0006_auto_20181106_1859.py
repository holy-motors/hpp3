# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-06 18:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_professionalprofileactivation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professionalprofileactivation',
            name='user',
        ),
        migrations.DeleteModel(
            name='ProfessionalProfileActivation',
        ),
    ]
