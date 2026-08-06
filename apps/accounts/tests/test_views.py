from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import User


class AccountViewTests(TestCase):
    def test_register_view_creates_user_and_redirects_to_login(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "email": "web-register@example.com",
                "password": "StrongPassword123",
                "confirm_password": "StrongPassword123",
            },
        )

        self.assertRedirects(response, reverse("accounts:login"))
        self.assertTrue(
            User.objects.filter(email="web-register@example.com").exists()
        )

    def test_login_view_authenticates_user_and_redirects_home(self):
        User.objects.create_user(
            email="web-login@example.com",
            password="StrongPassword123",
        )

        response = self.client.post(
            reverse("accounts:login"),
            {
                "email": "web-login@example.com",
                "password": "StrongPassword123",
            },
        )

        self.assertRedirects(response, reverse("website:home"))
