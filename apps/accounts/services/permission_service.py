def has_role(user, role):

    if not hasattr(user, "profile"):
        return False

    return user.profile.role == role



def is_admin(user):

    return (
        user.is_superuser
        or has_role(user, "admin")
    )



def is_recruiter(user):

    return has_role(
        user,
        "recruiter"
    )



def is_client(user):

    return has_role(
        user,
        "client"
    )