from django.test import TestCase

from apps.accounts.models import User, Profile


class ProfileSignalTest(TestCase):

    def test_profile_created_when_user_created(self):

        user = User.objects.create_user(
            email="signal@test.com",
            password="password123"
        )

        self.assertTrue(
            Profile.objects.filter(
                user=user
            ).exists()
        )