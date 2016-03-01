from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import Hobby, HobbyReview, HobbyService


class HobbyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hobby
        fields = ('id', 'name', 'short_desc', 'text', 'status', 'suggested_age_lower',
                  'suggested_age_upper', 'available_to_gender')

        def create(self, validated_data):
            print "Create......."
            return Hobby.objects.create(**validated_data)


class HobbyServiceListSerializer(serializers.ModelSerializer):
    hobby_id = HobbyListSerializer()
    class Meta:
        model = HobbyService
        fields = ('id', 'hobby_id', 'user_id', 'nick_name', 'status', 'end_date', 'creation_timestamp')

        def create(self, validated_data):
            print "Create......."
            return HobbyService.objects.create(**validated_data)


class HobbyServiceUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = HobbyService
        fields = ('id', 'nick_name', 'status', 'end_date')
        lookup_field = ('id')
        read_only_fields = ('creation_timestamp', )

        def update(self, instance, validated_data):
            instance.nick_name = validated_data.get('nick_name', instance.nick_name)
            instance.status = validated_data.get('status', instance.status)
            instance.end_date = validated_data.get('end_date', instance.end_date)


class HobbyReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = HobbyReview
        fields = ('id', 'hobby_id', 'user_id', 'rating', 'comments')

        def create(self, validated_data):
            print "Create......."
            return HobbyReview.objects.create(**validated_data)