# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-14 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professionalprofile',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='professionalprofile',
            name='speciality',
            field=models.CharField(choices=[(1, 'Dental'), (2, 'Vision'), (3, 'Physical'), (4, 'Psychological')], default=1, max_length=120),
        ),
        migrations.AlterField(
            model_name='professionalprofile',
            name='full_name',
            field=models.CharField(max_length=120),
        ),
    ]
