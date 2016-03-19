from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import Program, ProgramReview, ProgramService, HealthCondition, ProgramComponent

from habits.serializers import HabitListSerializer
from hobbys.serializers import HobbyListSerializer
from routines.serializers import RoutineListSerializer
from challenges.serializers import ChallengeListSerializer

class ProgramListSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(max_length=245, use_url=True)
    class Meta:
        model = Program
        fields = ('id', 'name', 'short_desc', 'text', 'status', 'suggested_age_lower',
                  'suggested_age_upper', 'available_to_gender', 'health_condition_id', 'picture')

        def create(self, validated_data):
            print "Create......."
            return Program.objects.create(**validated_data)


class ProgramServiceListSerializer(serializers.ModelSerializer):

    program_id = ProgramListSerializer()

    class Meta:
        model = ProgramService
        fields = ('id', 'program_id', 'user_id', 'nick_name', 'status', 'end_date', 'creation_timestamp')


class NewProgramServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProgramService
        fields = ('id', 'program_id', 'user_id', 'nick_name', 'status', 'end_date', 'creation_timestamp')

        def create(self, validated_data):
            print "Create......."
            return ProgramService.objects.create(**validated_data)


class ProgramServiceUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProgramService
        fields = ('id', 'nick_name', 'status', 'end_date')
        lookup_field = ('id')
        read_only_fields = ('creation_timestamp', )

        def update(self, instance, validated_data):
            instance.nick_name = validated_data.get('nick_name', instance.nick_name)
            instance.status = validated_data.get('status', instance.status)
            instance.end_date = validated_data.get('end_date', instance.end_date)


class ProgramReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProgramReview
        fields = ('id', 'program_id', 'user_id', 'rating', 'comments')

        def create(self, validated_data):
            print "Create......."
            return ProgramReview.objects.create(**validated_data)


class HealthConditionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = HealthCondition
        fields = ('id','health_condition','body_part','gender')

        def create(self, validated_data):
            print "Create......."
            return HealthCondition.objects.create(**validated_data)


class ProgramComponentListSerializer(serializers.ModelSerializer):


    class Meta:
        model = ProgramComponent
        fields = ('id', 'program_id', 'component_type', 'component_id')


class NewProgramComponentSerializer(serializers.ModelSerializer):

    program_id = ProgramListSerializer()

    class Meta:
        model = ProgramComponent
        fields = ('id', 'program_id', 'component_type', 'component_id')

        def create(self, validated_data):
            print "Create......."
            return ProgramComponent.objects.create(**validated_data)
