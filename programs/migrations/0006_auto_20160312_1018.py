# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-12 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0005_auto_20160311_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcondition',
            name='body_part',
            field=models.CharField(choices=[('GENERAL', 'General'), ('HEAD', 'Head'), ('EYE', 'Eye'), ('NOSE', 'Nose'), ('CHEST', 'Chest'), ('TEETH', 'Teeth'), ('MOUTH', 'Mouth'), ('THROAT', 'Throat'), ('EAR', 'Ear'), ('SPINE', 'Spine'), ('NECK', 'Neck'), ('STOMACH', 'Stomach'), ('KNEE', 'Knee'), ('FEET', 'Feet')], default='General', help_text=' Body part, ex: eye', max_length=30),
        ),
        migrations.AlterField(
            model_name='program',
            name='health_condition_id',
            field=models.ForeignKey(help_text='each program is associated with a health condition', on_delete=django.db.models.deletion.CASCADE, to='programs.HealthCondition', unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='programcomponent',
            unique_together=set([('program_id', 'component_type', 'component_id')]),
        ),
    ]
