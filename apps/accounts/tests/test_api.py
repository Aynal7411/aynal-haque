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