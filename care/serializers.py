from rest_framework import serializers

from care.models import (
    Article,
    CenterRating,
    Event,
    EventRegistration,
    ReabilatationCenter,
    Tag,
)
from users.models import ContactData
from users.serializers import ContactDataSerializer, UserSerializer


class ReabilitationRetrieveSerializer(serializers.ModelSerializer):
    contact_data = ContactDataSerializer()

    class Meta:
        model = ReabilatationCenter
        fields = [
            "id",
            "name",
            "contact_data",
            "description",
            "specialisation",
            "schedule",
        ]

    def create(self, validated_data):
        contact_data = validated_data.pop("contact_data")
        contact = ContactData.objects.create(**contact_data)
        center = ReabilatationCenter.objects.create(
            contact_data=contact, **validated_data
        )
        return center

    def update(self, instance, validated_data):
        contact_data = validated_data.pop("contact_data")
        contact_serializer = ContactDataSerializer(
            instance.contact_data, contact_data, partial=True
        )
        contact_serializer.is_valid(raise_exception=True)
        contact_serializer.update(instance.contact_data, contact_data)
        super(ReabilitationRetrieveSerializer, self).update(instance, validated_data)
        return instance


class ReabilitationListSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    contact_data = ContactDataSerializer(read_only=True)

    class Meta:
        model = ReabilatationCenter
        fields = ["id", "name", "contact_data", "specialisation", "rating"]

    def get_rating(self, obj):
        all_ratings = CenterRating.objects.filter(center=obj)
        score = 0
        for rating in all_ratings:
            score += rating.rating
        try:
            return round(score / all_ratings.count(), 1)
        except ZeroDivisionError:
            return 0


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterRating
        fields = ["id", "rating", "text"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    tags_list = TagSerializer(read_only=True)

    class Meta:
        model = Article
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    contact_data = ContactDataSerializer()

    class Meta:
        model = Event
        fields = "__all__"

    def create(self, validated_data):
        contact_data = validated_data.pop("contact_data")
        contact = ContactData.objects.create(**contact_data)
        event = Event.objects.create(contact_data=contact, **validated_data)
        return event

    def update(self, instance, validated_data):
        contact_data = validated_data.pop("contact_data")
        contact_serializer = ContactDataSerializer(
            instance.contact_data, contact_data, partial=True
        )
        contact_serializer.is_valid(raise_exception=True)
        contact_serializer.update(instance.contact_data, contact_data)
        super(EventSerializer, self).update(instance, validated_data)
        return instance


class EventRegistrationSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = EventRegistration
        fields = ["id", "event", "user"]
        read_only_fields = ["user", "event"]
