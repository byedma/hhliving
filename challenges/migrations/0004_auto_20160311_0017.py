# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-11 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0003_challenge_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='picture',
            field=models.ImageField(default='pictures/HHLife2.png', max_length=254, upload_to='pictures/'),
        ),
    ]
