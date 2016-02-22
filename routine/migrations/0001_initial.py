# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='name of the routine, ex: Fast 2 days a week', max_length=50)),
                ('short_desc', models.CharField(help_text='brief description of the routine', max_length=500)),
                ('text', models.TextField(help_text='full text of the routine with risks and benefits applicable')),
                ('status', models.CharField(help_text='different statuses available for routine', max_length=2, choices=[('UC', 'UnderConstruction'), ('UR', 'UnderReview'), ('SU', 'Submitted'), ('PU', 'Published')])),
                ('suggested_age_lower', models.PositiveSmallIntegerField(help_text='identifies the subscribers lowest eligible age limit')),
                ('suggested_age_upper', models.PositiveSmallIntegerField(help_text='identifies the subscribers upper eligible age limit')),
                ('available_to_gender', models.CharField(help_text='identifies the eligible genders who can subscribe to this habit', max_length=1, choices=[('F', 'Female'), ('M', 'Male'), ('B', 'Both')])),
                ('suggested_timeoftheday', models.CharField(help_text='identifies the suggested time for the routine', max_length=1, choices=[('Y', 'Any Time of the Day'), ('E', 'Early Morning, Before 6 AM'), ('M', 'Morning, Between 6AM to 10 AM'), ('A', 'Afternoon, 12AM to 2PM'), ('V', 'Evening, 5PM to 7PM'), ('N', 'After 9PM')])),
                ('suggested_timefrequency', models.CharField(help_text='identifies the suggested frequency', max_length=1, choices=[('H', 'Hourly'), ('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly'), ('Y', 'Yearly')])),
                ('suggested_timeperiod', models.PositiveSmallIntegerField(help_text='In minutes, gives the suggested time period the routine should be done for')),
            ],
        ),
        migrations.CreateModel(
            name='RoutineReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.SmallIntegerField(help_text='identifies the customers rating', choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')])),
                ('comments', models.TextField(help_text='customers review comments', blank=True)),
                ('routine_id', models.ForeignKey(help_text='uniquely identifies the routine', to='routine.Routine')),
                ('user_id', models.ForeignKey(help_text='identifies the customer who gave the rating and wrote a review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoutineService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick_name', models.CharField(help_text='customer given name for the routine, like "my fasting routine"', max_length=50)),
                ('status', models.CharField(help_text='status of the routine status', max_length=15, choices=[('E', 'Effective'), ('D', 'Dormant'), ('C', 'Completed')])),
                ('end_date', models.DateField(blank=True)),
                ('creation_timestamp', models.DateTimeField(help_text='date and time when customer first subscribed to this Routine', auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(help_text='date and time when customer last updated this Routine', auto_now=True)),
                ('routine_id', models.ForeignKey(help_text='identifies the routine template to which customer subscribed to', to='routine.Routine')),
                ('user_id', models.ForeignKey(help_text='identifies the customer signed up for the routine', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
