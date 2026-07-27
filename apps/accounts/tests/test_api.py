from django.urls import reverse

from rest_framework.test import APITestCase


class RegisterAPITest(APITestCase):

    def test_register_user(self):

        response = self.client.post(
            "/api/accounts/register/",
            {
                "email": "api@test.com",
                "password": "password123"
            },
            format="json"
        )


        self.assertEqual(
            response.status_code,
            201
        )

from apps.accounts.models import User


def test_login_user(self):

    User.objects.create_user(
        email="login@test.com",
        password="password123",
    )

    response = self.client.post(
        "/api/accounts/login/",
        {
            "email": "login@test.com",
            "password": "password123",
        },
        format="json",
    )

    self.assertEqual(response.status_code, 200)

    self.assertIn("access", response.data)

    self.assertIn("refresh", response.data)       