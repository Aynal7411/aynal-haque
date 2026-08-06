from django.test import SimpleTestCase
from django.urls import resolve, reverse

from apps.accounts.api.views import LoginAPIView, RegisterAPIView
from apps.accounts.views.auth import login_view
from apps.contact.views import contact_view
from apps.website.views import home_view


class RouteTests(SimpleTestCase):
    def test_account_login_route_resolves(self):
        match = resolve(reverse("accounts:login"))

        self.assertEqual(match.func, login_view)

    def test_website_home_route_resolves(self):
        match = resolve(reverse("website:home"))

        self.assertEqual(match.func, home_view)

    def test_contact_route_resolves(self):
        match = resolve(reverse("contact:contact"))

        self.assertEqual(match.func, contact_view)

    def test_account_api_routes_resolve(self):
        register_match = resolve(reverse("accounts_api:register"))
        login_match = resolve(reverse("accounts_api:login"))

        self.assertEqual(register_match.func.view_class, RegisterAPIView)
        self.assertEqual(login_match.func.view_class, LoginAPIView)
