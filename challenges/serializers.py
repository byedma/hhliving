from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import Challenge, ChallengeReview, ChallengeService


class ChallengeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Challenge
        fields = ('id', 'name', 'short_desc', 'text', 'status', 'suggested_age_lower',
                  'suggested_age_upper', 'available_to_gender','start_date','can_be_recurring')

        def create(self, validated_data):
            print "Create......."
            return Challenge.objects.create(**validated_data)


class ChallengeServiceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChallengeService
        fields = ('id', 'challenge_id', 'user_id', 'nick_name', 'status', 'end_date', 'creation_timestamp',
                  'start_date','is_recurring','recurring_count','recurring_frequency')

        def create(self, validated_data):
            print "Create......."
            return ChallengeService.objects.create(**validated_data)


class ChallengeServiceUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChallengeService
        fields = ('id', 'nick_name', 'status', 'end_date','start_date',
                         'is_recurring','recurring_count','recurring_frequency')
        lookup_field = ('id')
        read_only_fields = ('creation_timestamp', )

        def update(self, instance, validated_data):
            instance.nick_name = validated_data.get('nick_name', instance.nick_name)
            instance.status = validated_data.get('status', instance.status)
            instance.end_date = validated_data.get('end_date', instance.end_date)
            instance.is_recurring = validated_data.get('is_recurring',instance.is_recurring)
            instance.recurring_count = validated_data.get('recurring_count',instance.recurring_count)
            instance.recurring_frequency = validated_data.get('recurring_frequency',instance.recurring_frequency)
            instance.start_date = validated_data.get('start_date',instance.start_date)
            instance.end_date = validated_data.get('end_date',instance.end_date)


class ChallengeReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChallengeReview
        fields = ('id', 'challenge_id', 'user_id', 'rating', 'comments')

        def create(self, validated_data):
            print "Create......."
            return ChallengeReview.objects.create(**validated_data)