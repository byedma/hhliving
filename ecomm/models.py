from __future__ import unicode_literals

from django.db import models

# Create your models here.

from library.models import Communication, Review
# Create your models here.


class Merchant(models.Model):
    merchant_category_choices = (
        ('Apparel', 'Apparel'), ('Food', 'Food'), ('HealthCare','HealthCare'), ('Pharmacy', 'Pharmacy'),
        ('Travel', 'Travel'), ('Beauty', 'Beauty'), ('Electronics', 'Electronics'), ('Kitchen', 'Kitchen'),
        ('Sports', 'Sports'), ('MedicalLab', 'MedicalLab')
    )
    merchant_name = models.CharField(max_length=30, unique=True, help_text='name of the merchant')
    merchant_desc = models.CharField(max_length=500, help_text='full description of merchant')
    merchant_category = models.CharField(max_length=20, choices=merchant_category_choices, help_text='identifies the merchant group')
    """ future extension - merchant_rating"""


class Product(models.Model):

    product_name = models.CharField(max_length=30, help_text='identifies the product')
    product_desc = models.CharField(max_length=500, help_text='description of the product')
    '''Think of this as subcategory of merchant_category Ex:'''
    product_category = models.CharField(max_length=20, help_text='the low level grouping of the product')
    price = models.DecimalField(null=True, max_digits=5, decimal_places=2, help_text='price of the product')
    price_points = models.SmallIntegerField(null=True, help_text="price in points")
    merchant_id = models.ForeignKey('Merchant')

    class Meta:
        unique_together = ('merchant_id', 'product_name')


class MerchantReview(Review):
    merchant_id = models.ForeignKey('Merchant')


class OfferCommunication(Communication):

    offer_status_choices = (
        ('A', 'Activated'),
        ('R', 'Redeemed'),
    )

    reward_type_choices = (
        ('CA', 'Cash'),
        ('PE', 'PercentOff'),
        ('PO', 'Points')
    )

    offer_status = models.CharField(choices=offer_status_choices, max_length=1, help_text='offer status after presented')
    reward_type = models.CharField(choices=reward_type_choices, max_length=2, help_text='offered reward type')
    benefit = models.DecimalField(max_digits=5, decimal_places=2, help_text='total points or cash or discount percentage offered')


class ProductReview(Review):
    product_id = models.ForeignKey('Product')
