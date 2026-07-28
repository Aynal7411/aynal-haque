from apps.accounts.models import Profile


def get_profile(user):
    return (
        Profile.objects.select_related("user")
        .get(user=user)
    )