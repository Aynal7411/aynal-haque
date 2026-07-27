from django.test import TestCase

from apps.accounts.models import User, Profile
from apps.accounts.services.permission_service import (
    has_role,
)


class PermissionTest(TestCase):

    def test_user_role(self):

        user = User.objects.create_user(
            email="client@test.com",
            password="password123"
        )

        user.profile.role = "client"
        user.profile.save()


        self.assertTrue(
            has_role(
                user,
                "client"
            )
        )