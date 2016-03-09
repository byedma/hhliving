# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-09 20:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hobbys', '0004_auto_20160309_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobbyservice',
            name='creation_timestamp',
            field=models.DateTimeField(auto_now_add=True, help_text='date and time customer first subscribed to this component'),
        ),
        migrations.AlterField(
            model_name='hobbyservice',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hobbyservice',
            name='last_update_timestamp',
            field=models.DateTimeField(auto_now=True, help_text='date and time customer last updated this component'),
        ),
        migrations.AlterField(
            model_name='hobbyservice',
            name='nick_name',
            field=models.CharField(help_text='customer given name for the component, like "my diabetes type2 program"', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hobbyservice',
            name='status',
            field=models.CharField(choices=[('E', 'Effective'), ('D', 'Dormant'), ('C', 'Completed')], help_text='status of the program status', max_length=1),
        ),
        migrations.AlterField(
            model_name='hobbyservice',
            name='user_id',
            field=models.ForeignKey(help_text='identifies the customer signed up for the program', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
