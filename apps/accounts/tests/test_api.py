from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.accounts.models import User


class RegisterAPITest(APITestCase):
    def test_register_user(self):
        response = self.client.post(
            reverse("accounts_api:register"),
            {
                "email": "api@test.com",
                "password": "password123",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(email="api@test.com").exists())

    def test_register_user_requires_email_and_password(self):
        response = self.client.post(
            reverse("accounts_api:register"),
            {},
            format="json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("email", response.data)
        self.assertIn("password", response.data)

    def test_login_user(self):
        User.objects.create_user(
            email="login@test.com",
            password="password123",
        )

        response = self.client.post(
            reverse("accounts_api:login"),
            {
                "email": "login@test.com",
                "password": "password123",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_login_user_rejects_invalid_credentials(self):
        User.objects.create_user(
            email="login@test.com",
            password="password123",
        )

        response = self.client.post(
            reverse("accounts_api:login"),
            {
                "email": "login@test.com",
                "password": "wrong-password",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data["detail"], "Invalid email or password.")

    def test_access_token_can_be_validated(self):
        user = User.objects.create_user(
            email="jwt@test.com",
            password="password123",
        )

        response = self.client.post(
            reverse("accounts_api:login"),
            {
                "email": user.email,
                "password": "password123",
            },
            format="json",
        )

        token = JWTAuthentication().get_validated_token(response.data["access"])

        self.assertEqual(str(token["user_id"]), str(user.id))
