# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_auto_20160223_1736'),
        ('challenges', '0002_auto_20160223_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeReview',
            fields=[
                ('review_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='programs.Review')),
                ('challenge_id', models.ForeignKey(help_text='uniquely identifies the challenge', to='challenges.Challenge')),
            ],
            bases=('programs.review',),
        ),
        migrations.CreateModel(
            name='ChallengeService',
            fields=[
                ('service_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='programs.Service')),
                ('creation_timestamp', models.DateTimeField(help_text='date and time when customer first subscribed to this Challenge', auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(help_text='date and time when customer last updated this Challenge', auto_now=True)),
                ('start_date', models.DateField(help_text='date on which the event is happening, for recurring, start date')),
                ('end_Date', models.DateField(help_text='optional end date, used for recurring events only', null=True)),
                ('is_recurring', models.NullBooleanField(help_text='when true, identifies it as recurring event')),
                ('recurring_count', models.SmallIntegerField(help_text='how many times the event occurs', null=True)),
                ('recurring_frequency', models.CharField(help_text='identifies the frequency with which the event occurs', max_length=1, null=True, choices=[('H', 'Hourly'), ('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly'), ('Y', 'Yearly')])),
                ('challenge_id', models.ForeignKey(help_text='identifies the challenge template to which customer subscribed to', to='challenges.Challenge')),
            ],
            bases=('programs.service',),
        ),
    ]
