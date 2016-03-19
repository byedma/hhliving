from __future__ import unicode_literals

from django.db import models

from library.models import HealthComponent, HealthService, Review, gender_choices

# Create your models here.

''' ***Habit***'''


class HabitManager(models.Manager):

    def create(self, **validated_data):
        """
        Creates and saves circle.
        """

        Habit = self.model(
            name = validated_data.get('name', None),
            short_desc = validated_data.get('short_desc', None),
            text = validated_data.get('text', None),
            status = validated_data.get('status', None),
            is_bad_habit = validated_data.get('is_bad_habit', None),
            suggested_age_lower = validated_data.get('suggested_age_lower', None),
            suggested_age_upper = validated_data.get('suggested_age_upper', None),
            available_to_gender = validated_data.get('available_to_gender', None),
            picture = validated_data.get('picture', None),
        )

        Habit.save(using=self._db)
        return Habit


class Habit(HealthComponent):

    is_bad_habit = models.BooleanField(default=False, help_text='identifies as bad habit when true',)
    objects = HabitManager()

''' ***Service***'''


class HabitServiceManager(models.Manager):

    def create(self, **validated_data):
        """
        Creates and saves circle.
        """

        HabitService = self.model(
            habit_id = validated_data.get('habit_id', None),
            user_id = validated_data.get('user_id', None),
            nick_name = validated_data.get('nick_name', None),
            status = validated_data.get('status', None),
            end_date = validated_data.get('end_date', None),
        )

        HabitService.save(using=self._db)
        return HabitService


class HabitService(HealthService):

    # default id field generated by django serves as uniquely identifying field for habit service
    objects = HabitServiceManager()
    habit_id = models.ForeignKey('Habit', on_delete=models.CASCADE,
                                 help_text='identifies the habit template to which customer subscribed to')

    class Meta:
        unique_together = ('habit_id', 'user_id',)


''' ***Review***'''


class HabitReviewManager(models.Manager):

    def create(self, **validated_data):
        """
        Creates and saves circle.
        """

        HabitReview = self.model(
            habit_id = validated_data.get('habit_id', None),
            user_id = validated_data.get('user_id', None),
            rating = validated_data.get('rating', None),
            comments = validated_data.get('comments', None),
        )

        HabitReview.save(using=self._db)
        return HabitReview


class HabitReview(Review):
    # default id field generated by django serves as uniquely identifying field for habit review
    objects = HabitReviewManager()
    habit_id = models.ForeignKey('Habit', on_delete=models.CASCADE,
                                 help_text='uniquely identifies the habit')

    class Meta:
        unique_together = ('habit_id', 'user_id',)

