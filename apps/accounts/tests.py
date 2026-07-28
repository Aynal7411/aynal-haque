from django.test import SimpleTestCase
from django.urls import reverse


class AccountRouteTests(SimpleTestCase):
    def test_login_alias_route_resolves(self):
        response = self.client.get(reverse("login"))

        self.assertEqual(response.status_code, 200)
