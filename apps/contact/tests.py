from django.test import SimpleTestCase
from django.urls import reverse


class ContactPageTests(SimpleTestCase):
    def test_contact_page_renders_form(self):
        response = self.client.get(reverse("contact:contact"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Let us talk")
        self.assertContains(response, 'name="name"')
        self.assertContains(response, 'name="email"')
        self.assertContains(response, 'name="message"')

    def test_contact_page_shows_validation_errors(self):
        response = self.client.post(reverse("contact:contact"), {})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required")
