# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramComponent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('component_type', models.CharField(help_text='Identifies the type of the component', max_length=2, choices=[('HA', 'Habit'), ('HO', 'Hobby'), ('RO', 'Routine'), ('CH', 'Challenge')])),
                ('component_id', models.IntegerField(help_text='identifies the unique component like a Habit or Hobby')),
                ('program_id', models.ForeignKey(help_text='Identifies the program, this row component is associated with', to='programs.Program')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick_name', models.CharField(help_text='customer given name for the program, like "my diabetes type2 program"', max_length=50)),
                ('status', models.CharField(help_text='status of the program status', max_length=1, choices=[('E', 'Effective'), ('D', 'Dormant'), ('C', 'Completed')])),
                ('end_date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramService',
            fields=[
                ('service_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='programs.Service')),
                ('creation_timestamp', models.DateTimeField(help_text='date and time when customer first subscribed to this program', auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(help_text='date and time when customer last updated this program', auto_now=True)),
                ('program_id', models.ForeignKey(help_text='identifies the program template to which customer subscribed to', to='programs.Program')),
            ],
            bases=('programs.service',),
        ),
        migrations.AddField(
            model_name='service',
            name='user_id',
            field=models.ForeignKey(help_text='identifies the customer signed up for the program', to=settings.AUTH_USER_MODEL),
        ),
    ]
