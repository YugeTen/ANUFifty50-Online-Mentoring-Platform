# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 12:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0013_remove_profile_emails'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='emails',
            field=models.EmailField(default='needs@email.com', max_length=50, validators=[django.core.validators.RegexValidator('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$)', 'Only alphanumeric characters are allowed.')]),
        ),
    ]
