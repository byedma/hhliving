# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(help_text='different statuses available for challenge', max_length=2, choices=[('UC', 'UnderConstruction'), ('UR', 'UnderReview'), ('SU', 'Submitted'), ('PU', 'Published')])),
                ('start_date', models.DateField(help_text='date on which the event is happening, for recurring, start date', null=True)),
                ('can_be_recurring', models.BooleanField(default=False, help_text='when true identifies the challenge as can be used as recurring event')),
            ],
        ),
    ]
