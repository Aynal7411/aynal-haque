from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from apps.accounts.models import User


def register_user(
    email,
    password,
    **extra_fields
):
    """
    Create new user.
    """

    user = User.objects.create_user(
        email=email,
        password=password,
        **extra_fields
    )

    return user



def authenticate_user(
    request,
    email,
    password
):
    """
    Authenticate user and create session.
    """

    user = authenticate(
        request,
        username=email,
        password=password
    )

    if user:
        login(request, user)

    return user



def logout_user(request):
    """
    Destroy user session.
    """

    logout(request)

def generate_tokens(user):

    refresh = RefreshToken.for_user(user)

    return {

        "refresh": str(refresh),

        "access": str(refresh.access_token),

    }    