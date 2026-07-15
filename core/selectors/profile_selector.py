from core.models import Profile


def get_primary_profile():
    """
    Return the primary portfolio profile.
    """
    return Profile.objects.order_by("id").first()