from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import Routine, RoutineReview, RoutineService


class RoutineListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routine
        fields = ('id', 'name', 'short_desc', 'text', 'status', 'suggested_age_lower',
                  'suggested_age_upper', 'available_to_gender','suggested_timeoftheday','suggested_timefrequency','suggested_timeperiod')

        def create(self, validated_data):
            print "Create......."
            return Routine.objects.create(**validated_data)


class RoutineServiceListSerializer(serializers.ModelSerializer):
    routine_id = RoutineListSerializer()
    class Meta:
        model = RoutineService
        fields = ('id', 'routine_id', 'user_id', 'nick_name', 'status', 'end_date', 'creation_timestamp')

        def create(self, validated_data):
            print "Create......."
            return RoutineService.objects.create(**validated_data)


class RoutineServiceUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoutineService
        fields = ('id', 'nick_name', 'status', 'end_date')
        lookup_field = ('id')
        read_only_fields = ('creation_timestamp', )

        def update(self, instance, validated_data):
            instance.nick_name = validated_data.get('nick_name', instance.nick_name)
            instance.status = validated_data.get('status', instance.status)
            instance.end_date = validated_data.get('end_date', instance.end_date)


class RoutineReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoutineReview
        fields = ('id', 'routine_id', 'user_id', 'rating', 'comments')

        def create(self, validated_data):
            print "Create......."
            return RoutineReview.objects.create(**validated_data)