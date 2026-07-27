from django.test import TestCase

from apps.accounts.models import User
from apps.accounts.services.auth_service import register_user



class AuthenticationTest(TestCase):

    def test_user_registration(self):

        user = register_user(
            email="test@example.com",
            password="StrongPassword123"
        )

        self.assertEqual(
            user.email,
            "test@example.com"
        )

        self.assertTrue(
            user.check_password(
                "StrongPassword123"
            )
        )