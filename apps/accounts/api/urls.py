from django.urls import path

from apps.accounts.api.views import (
    LoginAPIView,
    RegisterAPIView,
)


app_name = "accounts_api"

urlpatterns = [
    path(
        "register/",
        RegisterAPIView.as_view(),
        name="register",
    ),
    path(
        "login/",
        LoginAPIView.as_view(),
        name="login",
    ),
]