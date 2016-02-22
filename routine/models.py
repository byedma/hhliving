from __future__ import unicode_literals

# Create your models here.

import uuid
from django.db import models

"""Routine is a template, Once customer subscribes to it, Routine Service will be created"""
routine_gender_choices = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('B', 'Both')
    )

class RoutineManager(models.Manager):

    def create(self, **validated_data):
        """
        Creates and saves routine
        """

        Routine = self.model(
            name = validated_data.get('name', None),
            short_desc = validated_data.get('short_desc', None),
            text = validated_data.get('text', None),
            status = validated_data.get('status', None),
            suggested_age_lower = validated_data.get('suggested_age_lower', None),
            suggested_age_upper = validated_data.get('suggested_age_upper', None),
            available_to_gender = validated_data.get('available_to_gender', None),
            suggested_timeoftheday = validated_data.get('suggested_timeoftheday', None),
            suggested_timefrequency = validated_data.get('suggested_frequency', None),
            suggested_timeperiod = validated_data.get('suggested_timeperiod', None),

        )

        Routine.save(using=self._db)
        return Routine

class Routine(models.Model):

    routine_status_choices = (
        ('UC', 'UnderConstruction'),
        ('UR', 'UnderReview'),
        ('SU', 'Submitted'),
        ('PU', 'Published'),
    )
    routine_time_choices = (
        ('Y', 'Any Time of the Day'),
        ('E', 'Early Morning, Before 6 AM'),
        ('M', 'Morning, Between 6AM to 10 AM'),
        ('A', 'Afternoon, 12AM to 2PM'),
        ('V', 'Evening, 5PM to 7PM'),
        ('N', 'After 9PM')
    )
    routine_frequency_choices = (
        ('H', 'Hourly'),
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('Y', 'Yearly')
    )


    name = models.CharField(max_length=50, help_text='name of the routine, ex: Fast 2 days a week',)
    short_desc = models.CharField(max_length=500, help_text='brief description of the routine',)
    text = models.TextField(help_text='full text of the routine with risks and benefits applicable',)
    status = models.CharField(max_length=2, choices=routine_status_choices,
                              help_text='different statuses available for routine')
    suggested_age_lower = models.PositiveSmallIntegerField(help_text='identifies the subscribers lowest eligible age limit',)
    suggested_age_upper = models.PositiveSmallIntegerField(help_text='identifies the subscribers upper eligible age limit',)
    available_to_gender = models.CharField(max_length=1, choices=routine_gender_choices,
                                           help_text='identifies the eligible genders who can subscribe to this habit',)
    suggested_timeoftheday = models.CharField(max_length=1, choices=routine_time_choices, help_text="identifies the suggested time for the routine",)
    suggested_timefrequency = models.CharField(max_length=1, choices=routine_frequency_choices, help_text="identifies the suggested frequency",)
    suggested_timeperiod = models.PositiveSmallIntegerField(help_text='In minutes, gives the suggested time period the routine should be done for')


class RoutineServiceManager(models.Manager):

    def create(self, **validated_data):
        """
        Creates and saves Routine service.
        """

        RoutineService = self.model(
            routine_id = validated_data.get('routine_id', None),
            user_id = validated_data.get('user_id', None),
            nick_name = validated_data.get('nick_name', None),
            status = validated_data.get('status', None),
            end_date = validated_data.get('end_date', None),
        )

        RoutineService.save(using=self._db)
        return RoutineService

class RoutineService(models.Model):
    routine_service_status_choices = (
        ('E', 'Effective'), ('D', 'Dormant'), ('C', 'Completed')
    )
    routine_id = models.ForeignKey('Routine', on_delete=models.CASCADE,
                                   help_text='identifies the routine template to which customer subscribed to',)
    user_id = models.ForeignKey('users.HUser', on_delete=models.CASCADE,
                                      help_text='identifies the customer signed up for the routine',)
    nick_name = models.CharField(max_length=50,
                                 help_text='customer given name for the routine, like "my fasting routine"')
    status = models.CharField(max_length=15, choices=routine_service_status_choices,
                              help_text='status of the routine status')
    end_date = models.DateField(blank=True, help_text='')
    creation_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False,
                                              help_text='date and time when customer first subscribed to this Routine',)

    last_update_timestamp = models.DateTimeField(auto_now_add=False, auto_now=True,
                                                 help_text='date and time when customer last updated this Routine',)

class RoutineReviewManager(models.Manager):

    def create(self, **validated_data):
        """
        Creates and saves Routine review.
        """

        RoutineReview = self.model(
            routine_id = validated_data.get('routine_id', None),
            user_id = validated_data.get('user_id', None),
            rating = validated_data.get('rating', None),
            comments = validated_data.get('comments', None),
        )

        RoutineReview.save(using=self._db)
        return RoutineReview



class RoutineReview(models.Model):
    rating_choices = (
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****')
    )
    routine_id = models.ForeignKey('Routine', on_delete=models.CASCADE,
                                   help_text='uniquely identifies the routine')
    user_id = models.ForeignKey('users.HUser', on_delete=models.CASCADE,
                                      help_text='identifies the customer who gave the rating and wrote a review',)
    rating = models.SmallIntegerField(choices=rating_choices, help_text='identifies the customers rating',)
    comments = models.TextField(blank=True, help_text='customers review comments',)
