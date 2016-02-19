# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hobbyreview',
            old_name='customer_id',
            new_name='user_id',
        ),
    ]
