# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-10 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobbys', '0006_auto_20160309_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobby',
            name='picture',
            field=models.ImageField(max_length=254, null=True, upload_to='pictures'),
        ),
    ]
