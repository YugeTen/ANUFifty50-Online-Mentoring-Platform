# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-28 04:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pair', '0004_auto_20170628_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pair',
            name='mentee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pair.Mentee', unique=True),
        ),
        migrations.AlterField(
            model_name='pair',
            name='mentor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pair.Mentor', unique=True),
        ),
    ]
