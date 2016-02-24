# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_programreview_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programreview',
            old_name='challenge_id',
            new_name='program_id',
        ),
        migrations.RemoveField(
            model_name='programreview',
            name='id',
        ),
        migrations.AddField(
            model_name='programreview',
            name='review_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='programs.Review'),
            preserve_default=False,
        ),
    ]
