from django.test import TestCase

from apps.accounts.models import User
from apps.accounts.services.auth_service import register_user


class AuthenticationTest(TestCase):
    def test_user_registration(self):
        user = register_user(
            email="test@example.com",
            password="StrongPassword123",
        )

        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("StrongPassword123"))
        self.assertTrue(user.username)

    def test_registration_generates_unique_usernames(self):
        first_user = register_user(
            email="same@example.com",
            password="StrongPassword123",
        )
        second_user = register_user(
            email="same@example.org",
            password="StrongPassword123",
        )

        self.assertEqual(first_user.username, "same")
        self.assertEqual(second_user.username, "same-1")

    def test_registration_accepts_explicit_username(self):
        user = User.objects.create_user(
            email="named@example.com",
            password="StrongPassword123",
            username="custom-name",
        )

        self.assertEqual(user.username, "custom-name")
