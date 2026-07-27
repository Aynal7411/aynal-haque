from rest_framework import serializers

from apps.accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
        ]

        read_only_fields = [
            "id",
        ]