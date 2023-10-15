from rest_framework import serializers

from users.models import ContactData


class ContactDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactData
        fields = "__all__"
