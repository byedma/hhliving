# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_auto_20160223_1736'),
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='id',
        ),
        migrations.AddField(
            model_name='challenge',
            name='servicetemplate_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='programs.ServiceTemplate'),
            preserve_default=False,
        ),
    ]
