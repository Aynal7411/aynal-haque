from django.urls import path

from apps.accounts.views.auth import (
    register_view,
    login_view,
    logout_view,
)

from apps.accounts.views.profile import (
    profile_view,
    edit_profile_view,
    change_password_view,
)

app_name = "accounts"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    path("profile/", profile_view, name="profile"),
    path("profile/edit/", edit_profile_view, name="profile_edit"),
    path("change-password/", change_password_view, name="change_password"),
]