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
            name='Habit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='name of the habit, ex: Smoking, Overspending, Jogging', max_length=50)),
                ('short_desc', models.CharField(help_text='brief description of the habit', max_length=500)),
                ('text', models.TextField(help_text='full text of the habit with risks and benefits applicable')),
                ('status', models.CharField(help_text='different statuses available for habit', max_length=2, choices=[('UC', 'UnderConstruction'), ('UR', 'UnderReview'), ('SU', 'Submitted'), ('PU', 'Published')])),
                ('is_bad_habit', models.BooleanField(default=False, help_text='identifies as bad habit when true')),
                ('suggested_age_lower', models.SmallIntegerField(help_text='identifies the subscribers lowest eligible age limit')),
                ('suggested_age_upper', models.SmallIntegerField(help_text='identifies the subscribers upper eligible age limit')),
                ('available_to_gender', models.CharField(help_text='identifies the eligible genders who can subscribe to this habit', max_length=1, choices=[('F', 'Female'), ('M', 'Male'), ('B', 'Both')])),
            ],
        ),
        migrations.CreateModel(
            name='HabitReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.SmallIntegerField(help_text='identifies the customers rating', choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')])),
                ('comments', models.TextField(help_text='customers review comments', blank=True)),
                ('habit_id', models.ForeignKey(help_text='uniquely identifies the habit', to='habits.Habit')),
                ('user_id', models.ForeignKey(help_text='identifies the customer who gave the rating and wrote a review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HabitService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick_name', models.CharField(help_text='customer given name for the habit, like "my smoking habit"', max_length=50)),
                ('status', models.CharField(help_text='status of the habit status', max_length=1, choices=[('E', 'Effective'), ('D', 'Dormant'), ('C', 'Completed')])),
                ('end_date', models.DateField(blank=True)),
                ('creation_timestamp', models.DateTimeField(help_text='date and time when customer first subscribed to this Habit', auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(help_text='date and time when customer last updated this Habit', auto_now=True)),
                ('habit_id', models.ForeignKey(help_text='identifies the habit template to which customer subscribed to', to='habits.Habit')),
                ('user_id', models.ForeignKey(help_text='identifies the customer signed up for the habit', to=settings.AUTH_USER_MODEL)),
            ],
        )
    ]
