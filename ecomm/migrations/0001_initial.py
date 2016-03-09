# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-09 22:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_name', models.CharField(help_text='name of the merchant', max_length=30, unique=True)),
                ('merchant_desc', models.CharField(help_text='full description of merchant', max_length=500)),
                ('merchant_category', models.CharField(choices=[('Apparel', 'Apparel'), ('Food', 'Food'), ('HealthCare', 'HealthCare'), ('Pharmacy', 'Pharmacy'), ('Travel', 'Travel'), ('Beauty', 'Beauty'), ('Electronics', 'Electronics'), ('Kitchen', 'Kitchen'), ('Sports', 'Sports'), ('MedicalLab', 'MedicalLab')], help_text='identifies the merchant group', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MerchantReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], help_text='identifies the users rating')),
                ('comments', models.TextField(blank=True, help_text='users review comments', null=True)),
                ('merchant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomm.Merchant')),
                ('user_id', models.ForeignKey(help_text='identifies the user who gave the rating and worote a review', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OfferCommunication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_start_date', models.DateField(help_text='date on which the communication is first created')),
                ('valid_end_date', models.DateField(help_text='date on which communication becomes invalid, becomes candidate for purging', null=True)),
                ('communication_status', models.CharField(choices=[('R', 'read'), ('U', 'unread'), ('A', 'acted')], default='U', help_text='choice of the communication status', max_length=1)),
                ('offer_status', models.CharField(choices=[('A', 'Activated'), ('R', 'Redeemed')], help_text='offer status after presented', max_length=1)),
                ('reward_type', models.CharField(choices=[('CA', 'Cash'), ('PE', 'PercentOff'), ('PO', 'Points')], help_text='offered reward type', max_length=2)),
                ('benefit', models.DecimalField(decimal_places=2, help_text='total points or cash or discount percentage offered', max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(help_text='identifies the product', max_length=30)),
                ('product_desc', models.CharField(help_text='description of the product', max_length=500)),
                ('product_category', models.CharField(help_text='the low level grouping of the product', max_length=20)),
                ('price', models.DecimalField(decimal_places=2, help_text='price of the product', max_digits=5, null=True)),
                ('price_points', models.SmallIntegerField(help_text='price in points', null=True)),
                ('merchant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomm.Merchant')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], help_text='identifies the users rating')),
                ('comments', models.TextField(blank=True, help_text='users review comments', null=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomm.Product')),
                ('user_id', models.ForeignKey(help_text='identifies the user who gave the rating and worote a review', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('merchant_id', 'product_name')]),
        ),
    ]