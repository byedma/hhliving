from __future__ import unicode_literals

# Create your models here.

from django.db import models
from library.models import HealthComponent, HealthService, Review

"""Challenge is a template, Once customer subscribes to it, Challenge Service will be created"""


challenge_frequency_choices = (
        ('H', 'Hourly'),
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('Y', 'Yearly')
    )

class ChallengeManager(models.Manager):
    def create(self,**validated_data):
        Challenge = self.model(
            name = validated_data.get('name', None),
            short_desc = validated_data.get('short_desc', None),
            text = validated_data.get('text', None),
            status = validated_data.get('status', None),
            suggested_age_lower = validated_data.get('suggested_age_lower', None),
            suggested_age_upper = validated_data.get('suggested_age_upper', None),
            available_to_gender = validated_data.get('available_to_gender', None),
            start_date = validated_data.get('start_date',None),
            can_be_recurring = validated_data.get('can_be_recurring',None)
        )
        Challenge.save(using=self._db)
        return Challenge


class Challenge(HealthComponent):
    #default id field generated by django, serves as uniquely identifying field for challenge
    start_date = models.DateField(null=True, help_text='date on which the event is happening, for recurring, start date')
    can_be_recurring = models.BooleanField(default=False, help_text='when true identifies the challenge as can be used as recurring event')

    objects = ChallengeManager()

class ChallengeServiceManager(models.Manager):

    def create(self, **validated_data):
        """
        Creates and saves challenge service.
        """

        ChallengeService = self.model(
            challenge_id = validated_data.get('challenge_id', None),
            user_id = validated_data.get('user_id', None),
            nick_name = validated_data.get('nick_name', None),
            status = validated_data.get('status', None),
            end_date = validated_data.get('end_date', None),
            start_date = validated_data.get('start_date',None),
            is_recurring = validated_data.get('is_recurring',None),
            recurring_count = validated_data.get('recurring_count',None),
            recurring_frequency = validated_data.get('recurring_frequency',None),
        )

        ChallengeService.save(using=self._db)
        return ChallengeService


class ChallengeService(HealthService):
    #default id field generated by django serves as uniquely identifying field for challenge service
    challenge_id = models.ForeignKey('Challenge', on_delete=models.CASCADE,
                                 help_text='identifies the challenge template to which customer subscribed to',)
    start_date = models.DateField(help_text='date on which the event is happening, for recurring, start date')
    end_Date = models.DateField(null=True, help_text='optional end date, used for recurring events only')
    is_recurring = models.NullBooleanField(null=True, help_text='when true, identifies it as recurring event')
    recurring_count = models.SmallIntegerField(null=True, help_text='how many times the event occurs')
    recurring_frequency = models.CharField(max_length=1, null=True, choices=challenge_frequency_choices,
                                           help_text='identifies the frequency with which the event occurs')
    objects = ChallengeServiceManager()

    class Meta:
        unique_together = ('challenge_id', 'user_id',)

class ChallengeReviewManager(models.Manager):
    def create(self,**validated_data):
        ChallengeReview = self.model(
            challenge_id = validated_data.get('challenge_id'),
            user_id = validated_data.get('user_id', None),
            rating = validated_data.get('rating', None),
            comments = validated_data.get('comments', None),
        )
        ChallengeReview.save(using=self._db)
        return ChallengeReview



class ChallengeReview(Review):
    #default id field generated by django serves as uniquely identifying field for challenge review
    challenge_id = models.ForeignKey('Challenge', on_delete=models.CASCADE,
                                 help_text='uniquely identifies the challenge')
    objects = ChallengeReviewManager()

    class Meta:
        unique_together = ('challenge_id', 'user_id',)


