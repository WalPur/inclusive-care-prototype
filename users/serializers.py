from rest_framework import serializers

from users.models import ContactData, CustomUser


class ContactDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactData
        fields = "__all__"


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "password"]


class UserSerializer(serializers.ModelSerializer):
    contact_data = ContactDataSerializer()

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "last_name",
            "first_name",
            "middle_name",
            "date_of_birth",
            "gender",
            "contact_data",
        ]
