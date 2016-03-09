from __future__ import unicode_literals

# Create your models here.

import uuid
from django.db import models
from library.models import HealthComponent, HealthService, Review, gender_choices

"""Routine is a template, Once customer subscribes to it, Routine Service will be created"""
'''***Routine***'''


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


class Routine(HealthComponent):
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
    suggested_timeoftheday = models.CharField(max_length=1, choices=routine_time_choices, help_text="identifies the suggested time for the routine",)
    suggested_timefrequency = models.CharField(max_length=1, choices=routine_frequency_choices, help_text="identifies the suggested frequency",)
    suggested_timeperiod = models.PositiveSmallIntegerField(help_text='In minutes, gives the suggested time period the routine should be done for')
    objects = RoutineManager()


'''***Service***'''


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


class RoutineService(HealthService):

    # default id field generated by django serves as uniquely identifying field for routine service
    objects = RoutineServiceManager()
    routine_id = models.ForeignKey('Routine', on_delete=models.CASCADE,
                                 help_text='identifies the routine template to which customer subscribed to')

    class Meta:
        unique_together = ('routine_id', 'user_id',)

'''***Review***'''


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


class RoutineReview(Review):
    # default id field generated by django serves as uniquely identifying field for routine review
    objects = RoutineReviewManager()
    routine_id = models.ForeignKey('Routine', on_delete=models.CASCADE,
                                 help_text='uniquely identifies the routine')

    class Meta:
        unique_together = ('routine_id', 'user_id',)