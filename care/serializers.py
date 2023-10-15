from rest_framework import serializers

from care.models import CenterRating, ReabilatationCenter


class ReabilitationListSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()

    class Meta:
        model = ReabilatationCenter
        fields = ["name", "address", "specialisation", "rating"]

    def get_rating(self, obj):
        all_ratings = CenterRating.objects.filter(center=obj)
        score = 0
        for rating in all_ratings:
            score += rating.rating
        return round(score / all_ratings.count(), 1)

    def get_address(self, obj):
        return obj.contact_data.address


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CenterRating
        fields = ["rating", "text"]
