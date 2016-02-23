# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthCondition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('health_condition', models.CharField(help_text='health condition ex: Diabetes', max_length=50, choices=[('DIABETES-TYPE2', 'Diabetes Type2'), ('ARTHRITIS', 'Arthritis'), ('OSTEOPOROSIS', 'Osteoporosis'), ('ADHD', 'ADHD'), ('SLEEP-APNIA', 'Sleep Apnea')])),
                ('body_part', models.CharField(default='General', help_text=' Body part, ex: eye', max_length=30, choices=[('GENERAL', 'General'), ('HEAD', 'Head'), ('EYE', 'Eye'), ('NOSE', 'Nose'), ('CHEST', 'Chest')])),
                ('gender', models.CharField(default='B', help_text='gender ex: Female', max_length=1, choices=[('F', 'Female'), ('M', 'Male'), ('B', 'Both')])),
            ],
        ),
        migrations.CreateModel(
            name='ServiceTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name of the modeled program', max_length=50)),
                ('short_desc', models.CharField(max_length=500)),
                ('text', models.TextField(help_text='full text of the program with risks and benefits applicable')),
                ('suggested_age_lower', models.SmallIntegerField(help_text='identifies the subscribers lowest eligible age limit')),
                ('suggested_age_upper', models.SmallIntegerField(help_text='identifies the subscribers upper eligible age limit')),
                ('available_to_gender', models.CharField(help_text='identifies the eligible genders who can subscribe to this habit', max_length=1, choices=[('F', 'Female'), ('M', 'Male'), ('B', 'Both')])),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('servicetemplate_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='programs.ServiceTemplate')),
                ('status', models.CharField(help_text='different statuses available for program', max_length=2, choices=[('UC', 'UnderConstruction'), ('UR', 'UnderReview'), ('SU', 'Submitted'), ('PU', 'Published')])),
                ('creation_timestamp', models.DateTimeField(help_text='date and time when customer first subscribed to this Hobby', auto_now_add=True)),
                ('publish_timestamp', models.DateTimeField(help_text='date and time when customer first subscribed to this Hobby', null=True)),
            ],
            bases=('programs.servicetemplate',),
        ),
        migrations.AlterUniqueTogether(
            name='healthcondition',
            unique_together=set([('health_condition', 'body_part', 'gender')]),
        ),
        migrations.AddField(
            model_name='program',
            name='health_condition',
            field=models.ForeignKey(help_text='A program is prescribed based on health condition, body part, gender combination', to='programs.HealthCondition'),
        ),
    ]
