# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-02 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0033_auto_20170930_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='degree_programme',
            field=models.CharField(choices=[('', '-'), ('AACOM', 'Bachelor of Advanced Computing (Honours)'), ('AACRD', 'Bachelor of Advanced Computing (R&D) (Honours)'), ('BADAN', 'Bachelor of Applied Data Analytics'), ('HADAN', 'Bachelor of Applied Data Analytics (Honours)'), ('BBIOT', 'Bachelor of Biotechnology'), ('HBIOT', 'Bachelor of Biotechnology (Honours)'), ('AENGI', 'Bachelor of Engineering (Honours)'), ('AENRD', 'Bachelor of Engineering (R&D) (Honours)'), ('BENSU', 'Bachelor of Environment and Sustainability'), ('HENSU', 'Bachelor of Environment and Sustainability (Honours)'), ('AENSU', 'Bachelor of Environment and Sustainability Advanced (Honours)'), ('HENVS', 'Bachelor of Environemntal Studies'), ('BGENE', 'Bachelor of Genetics'), ('HGENE', 'Bachelor of Genetics (Honours)'), ('BHLTH', 'Bachelor of Health Science (Honours)'), ('BIT', 'Bachelor of Information Technology'), ('HIT', 'Bachelor of Information Technology (Honours)'), ('BMASC', 'Bachelor of Mathematical Sciences'), ('HMASC', 'Bachelor of Mathematical Sciences (Honours)'), ('BMEDS', 'Bachelor of Medical Science'), ('HMEDS/HMDSA', 'Bachelor of Medical Science (Honours)'), ('PHBSCIENCE', 'PhB / Bachelor of Philosophy (Honours) in Science'), ('APSYC', 'Bachelor of Psychology (Honours)'), ('BSC', 'Science'), ('HSC', 'Bachelor of Science (Honours)'), ('ASCAD', 'Bachelor of Science (Advanced) (Honours)'), ('BSPSY', 'Science (Psychology)'), ('HSPSY', 'Bachelor of Science (Psychology) (Honours)'), ('ASENG', 'Bachelor of Software Engineering (Honours)'), ('ESCIE', 'Diploma of Science'), ('ECOMP', 'Diploma of Computing')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='degree_programme_2',
            field=models.CharField(choices=[('', '-'), ('AACOM', 'Bachelor of Advanced Computing (Honours)'), ('AACRD', 'Bachelor of Advanced Computing (R&D) (Honours)'), ('BADAN', 'Bachelor of Applied Data Analytics'), ('HADAN', 'Bachelor of Applied Data Analytics (Honours)'), ('BBIOT', 'Bachelor of Biotechnology'), ('HBIOT', 'Bachelor of Biotechnology (Honours)'), ('AENGI', 'Bachelor of Engineering (Honours)'), ('AENRD', 'Bachelor of Engineering (R&D) (Honours)'), ('BENSU', 'Bachelor of Environment and Sustainability'), ('HENSU', 'Bachelor of Environment and Sustainability (Honours)'), ('AENSU', 'Bachelor of Environment and Sustainability Advanced (Honours)'), ('HENVS', 'Bachelor of Environemntal Studies'), ('BGENE', 'Bachelor of Genetics'), ('HGENE', 'Bachelor of Genetics (Honours)'), ('BHLTH', 'Bachelor of Health Science (Honours)'), ('BIT', 'Bachelor of Information Technology'), ('HIT', 'Bachelor of Information Technology (Honours)'), ('BMASC', 'Bachelor of Mathematical Sciences'), ('HMASC', 'Bachelor of Mathematical Sciences (Honours)'), ('BMEDS', 'Bachelor of Medical Science'), ('HMEDS/HMDSA', 'Bachelor of Medical Science (Honours)'), ('PHBSCIENCE', 'PhB / Bachelor of Philosophy (Honours) in Science'), ('APSYC', 'Bachelor of Psychology (Honours)'), ('BSC', 'Science'), ('HSC', 'Bachelor of Science (Honours)'), ('ASCAD', 'Bachelor of Science (Advanced) (Honours)'), ('BSPSY', 'Science (Psychology)'), ('HSPSY', 'Bachelor of Science (Psychology) (Honours)'), ('ASENG', 'Bachelor of Software Engineering (Honours)'), ('ESCIE', 'Diploma of Science'), ('ECOMP', 'Diploma of Computing')], max_length=50, null=True),
        ),
    ]
