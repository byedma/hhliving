# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-10 22:54
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='picture',
            field=models.ImageField(max_length=254, null=True, upload_to='pictures'),
        ),
    ]