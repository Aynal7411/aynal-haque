from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.accounts.models import User, Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Automatically create profile after user creation.
    """

    if created:
        Profile.objects.create(
            user=instance
        )


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Save profile whenever user is updated.
    """

    if hasattr(instance, "profile"):
        instance.profile.save()