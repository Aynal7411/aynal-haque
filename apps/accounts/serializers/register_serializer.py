from rest_framework import serializers

from apps.accounts.models import User


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True
    )


    class Meta:

        model = User

        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
        ]


    def create(self, validated_data):

        user = User.objects.create_user(
            **validated_data
        )

        return user