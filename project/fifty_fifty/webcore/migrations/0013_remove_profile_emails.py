# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 12:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0012_auto_20170430_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='emails',
        ),
    ]
