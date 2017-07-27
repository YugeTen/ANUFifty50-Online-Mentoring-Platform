# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-24 01:15
from __future__ import unicode_literals

from django.db import migrations, models
import resource_manager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Filename', models.CharField(blank=True, max_length=25)),
                ('Role', models.CharField(choices=[('Mentee', 'Mentee'), ('Mentor', 'Mentor'), ('Training', 'Training')], default='Mentee', max_length=25)),
                ('Week', models.CharField(choices=[('Week_1', 'Week_1'), ('Week_2', 'Week_2'), ('Week_3', 'Week_3'), ('Week_4', 'Week_4')], default='Week_1', max_length=10)),
                ('docfile', models.FileField(upload_to=resource_manager.models.Document.choices_location)),
            ],
        ),
    ]