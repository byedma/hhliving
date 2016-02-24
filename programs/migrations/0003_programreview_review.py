# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('programs', '0002_auto_20160223_0212'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('challenge_id', models.ForeignKey(help_text='uniquely identifies the program', to='programs.Program')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.SmallIntegerField(help_text='identifies the users rating', choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')])),
                ('comments', models.TextField(help_text='users review comments', blank=True)),
                ('user_id', models.ForeignKey(help_text='identifies the user who gave the rating and worote a review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
