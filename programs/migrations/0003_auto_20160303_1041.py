# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 10:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_program_health_condition_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='programreview',
            unique_together=set([('program_id', 'user_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='programservice',
            unique_together=set([('program_id', 'user_id')]),
        ),
    ]
