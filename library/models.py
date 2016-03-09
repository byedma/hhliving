from __future__ import unicode_literals

from django.db import models

# Create your models here.


# abstract starts
gender_choices = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('B', 'Both'),
    )

service_status_choices = (
       ('E', 'Effective'), ('D', 'Dormant'), ('C', 'Completed')
    )

health_component_status_choices = (
        ('UC', 'UnderConstruction'),
        ('UR', 'UnderReview'),
        ('SU', 'Submitted'),
        ('PU', 'Published'),

    )


class HealthComponent(models.Model):
    name = models.CharField(max_length=50, help_text='Name of the modeled component')
    short_desc = models.CharField(max_length=500, help_text='')
    text = models.TextField(help_text='full text of the component with risks and benefits applicable',)
    suggested_age_lower = models.SmallIntegerField(help_text='identifies the subscribers lowest eligible age limit',)
    suggested_age_upper = models.SmallIntegerField(help_text='identifies the subscribers upper eligible age limit',)
    available_to_gender = models.CharField(max_length=1, choices=gender_choices,
                                           help_text='the eligible genders who can subscribe to this component',)
    status = models.CharField(max_length=2, choices=health_component_status_choices,
                              help_text='different statuses available for program')
    creation_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False,
                                              help_text='date and time customer first subscribed to this component',)
    #created at UnderConstruction or Submitted, publish timestamp after status is set to published
    publish_timestamp = models.DateTimeField(null=True,
                                             help_text='date and time customer first subscribed to this component',)

    class Meta:
        abstract = True


class HealthService(models.Model):

    user_id = models.ForeignKey('users.HUser', on_delete=models.CASCADE,
                                help_text='identifies the customer signed up for the program',)
    nick_name = models.CharField(null=True,  max_length=50,
                                 help_text='customer given name for the component, like "my diabetes type2 program"')
    status = models.CharField(max_length=1, choices=service_status_choices,
                              help_text='status of the program status')
    end_date = models.DateField(null=True, blank=True, help_text='')
    creation_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False,
                                              help_text='date and time customer first subscribed to this component',)
    last_update_timestamp = models.DateTimeField(auto_now_add=False, auto_now=True,
                                                 help_text='date and time customer last updated this component')

    class Meta:
        abstract = True


class Review(models.Model):
    rating_choices = (
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****')
    )
    user_id = models.ForeignKey('users.HUser', on_delete=models.CASCADE,
                                help_text='identifies the user who gave the rating and worote a review')
    rating = models.SmallIntegerField(choices=rating_choices,help_text='identifies the users rating')
    comments = models.TextField(null=True, blank=True, help_text='users review comments')

    class Meta:
        abstract = True


class Communication(models.Model):

    communication_status_choices = (
        ('R', 'read'),
        ('U', 'unread'),
        ('A', 'acted'),
    )

    valid_start_date = models.DateField(help_text='date on which the communication is first created')
    valid_end_date = models.DateField(null=True, help_text='date on which communication becomes invalid, becomes candidate for purging')
    communication_status = models.CharField(default='U',  max_length=1, choices=communication_status_choices,
                                    help_text='choice of the communication status')

    class Meta:
        abstract = True


# ends

