# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-10 10:43
# Generated by Django 1.11.1 on 2017-08-06 06:51
# Generated by Django 1.11 on 2017-08-11 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0019_auto_20170430_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Mentee', 'Mentee'), ('Mentor', 'Mentor')], max_length=15, null=True),
        ),
    ]
