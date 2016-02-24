from __future__ import unicode_literals

# Create your models here.

from django.db import models

program_gender_choices = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('B', 'Both'),
    )

class ServiceTemplate(models.Model):
    name = models.CharField(max_length=50, help_text='Name of the modeled program')
    short_desc = models.CharField(max_length=500, help_text='')
    text = models.TextField(help_text='full text of the program with risks and benefits applicable',)
    suggested_age_lower = models.SmallIntegerField(help_text='identifies the subscribers lowest eligible age limit',)
    suggested_age_upper = models.SmallIntegerField(help_text='identifies the subscribers upper eligible age limit',)
    available_to_gender = models.CharField(max_length=1, choices=program_gender_choices,
                                           help_text='identifies the eligible genders who can subscribe to this habit',)


class HealthConditinManager(models.Manager):
    def create(self,**validated_data):
        HealthCondition = self.model(
            health_condition = validated_data.get('health_condition',None),
            body_part = validated_data.get('body_part',None),
            gender = validated_data.get('gender',None)
        )

        HealthCondition.save(using=self._db)
        return HealthCondition


class HealthCondition(models.Model):

    health_condition_choices = (
        ('DIABETES-TYPE2', 'Diabetes Type2'),
        ('ARTHRITIS', 'Arthritis'),
        ('OSTEOPOROSIS', 'Osteoporosis'),
        ('ADHD', 'ADHD'),
        ('SLEEP-APNIA', 'Sleep Apnea'),
    )
    body_part_choices = (
        ('GENERAL', 'General'),
        ('HEAD', 'Head'),
        ('EYE', 'Eye'),
        ('NOSE', 'Nose'),
        ('CHEST', 'Chest'),
    )

    objects = HealthConditinManager()

    health_condition = models.CharField(max_length=50, choices=health_condition_choices,
                                        help_text='health condition ex: Diabetes',)
    body_part = models.CharField(max_length=30, choices=body_part_choices, default='General',
                                 help_text=' Body part, ex: eye',)
    gender = models.CharField(max_length=1, default='B', choices=program_gender_choices, help_text='gender ex: Female',)

    class Meta:
        unique_together = (('health_condition', 'body_part', 'gender'),)


class ProgramManger(models.Manager):
    def create(self,**validated_data):
        Program = self.model(
            name = validated_data.get('name', None),
            short_desc = validated_data.get('short_desc', None),
            text = validated_data.get('text', None),
            status = validated_data.get('status', None),
            suggested_age_lower = validated_data.get('suggested_age_lower', None),
            suggested_age_upper = validated_data.get('suggested_age_upper', None),
            available_to_gender = validated_data.get('available_to_gender', None),
            health_condition_id = validated_data.get('health_condition_id', None),

        )
        Program.save(using=self._db)
        return Program

class Program(ServiceTemplate):
    program_status_choices = (
        ('UC', 'UnderConstruction'),
        ('UR', 'UnderReview'),
        ('SU', 'Submitted'),
        ('PU', 'Published'),

    )
    objects = ProgramManger()
    status = models.CharField(max_length=2, choices=program_status_choices,
                              help_text='different statuses available for program')

    health_condition = models.ForeignKey('HealthCondition',
                                         help_text='A program is prescribed based on health condition, '
                                                   'body part, gender combination',)
    creation_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False,
                                              help_text='date and time when customer first subscribed to this Hobby',)
    #created at UnderConstruction or Submitted, publish timestamp after status is set to published
    publish_timestamp = models.DateTimeField(null=True,
                                             help_text='date and time when customer first subscribed to this Hobby',)

class ProgramComponentManager(models.Manager):
    def create(self,**validated_data):
        ProgramComponent = self.model(
            program_id = validated_data.get('program_id',None),
            component_type = validated_data.get('component_type',None),
            component_id = validated_data.get('component_id',None)
        )
        ProgramComponent.save(using=self._db)
        return ProgramComponent

class ProgramComponent(models.Model):
    component_type_choices =(
        ('HA','Habit'),
        ('HO','Hobby'),
        ('RO','Routine'),
        ('CH','Challenge'),
    )
    objects = ProgramComponentManager()
    program_id = models.ForeignKey('Program', help_text='Identifies the program, this row component is associated with')
    component_type = models.CharField(max_length=2, choices=component_type_choices,
                                      help_text='Identifies the type of the component')
    component_id = models.IntegerField(help_text='identifies the unique component like a Habit or Hobby')


class Service(models.Model):
    program_service_status_choices = (
       ('E', 'Effective'), ('D', 'Dormant'), ('C', 'Completed')
    )
    user_id = models.ForeignKey('users.HUser', on_delete=models.CASCADE,
                                      help_text='identifies the customer signed up for the program',)
    nick_name = models.CharField(max_length=50,
                                 help_text='customer given name for the program, like "my diabetes type2 program"')
    status = models.CharField(max_length=1, choices=program_service_status_choices,
                              help_text='status of the program status')
    end_date = models.DateField(blank=True, help_text='')


class ProgramServiceManager(models.Manager):
    def create(self,**validated_data):
        ProgramService = self.model(
            program_id = validated_data.get('program_id', None),
            user_id = validated_data.get('user_id', None),
            nick_name = validated_data.get('nick_name', None),
            status = validated_data.get('status', None),
            end_date = validated_data.get('end_date', None),
        )
        ProgramService.save(using=self._db)
        return ProgramService



class ProgramService(Service):
    #default id field generated by django serves as uniquely identifying field for program service
    objects = ProgramServiceManager()
    program_id = models.ForeignKey('Program', on_delete=models.CASCADE,
                                 help_text='identifies the program template to which customer subscribed to')
    creation_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False,
                                              help_text='date and time when customer first subscribed to this program',)

    last_update_timestamp = models.DateTimeField(auto_now_add=False, auto_now=True,
                                                 help_text='date and time when customer last updated this program')


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
    comments = models.TextField(blank=True, help_text='users review comments')


class ProgramReviewManager(models.Manager):

    def create(self, **validated_data):
        """
        Creates and saves program review.
        """

        ProgramReview = self.model(
            program_id = validated_data.get('program_id', None),
            user_id = validated_data.get('user_id', None),
            rating = validated_data.get('rating', None),
            comments = validated_data.get('comments', None),
        )

        ProgramReview.save(using=self._db)
        return ProgramReview





class ProgramReview(Review):
    #default id field generated by django serves as uniquely identifying field for program review
    objects = ProgramReviewManager()
    program_id = models.ForeignKey('Program', on_delete=models.CASCADE,
                                 help_text='uniquely identifies the program')

