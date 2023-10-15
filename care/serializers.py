from rest_framework import serializers

from care.models import CenterRating, ReabilatationCenter
from users.models import ContactData
from users.serializers import ContactDataSerializer


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
        return round(score / all_ratings.count(), 1)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterRating
        fields = ["rating", "text"]
