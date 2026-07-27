from django.urls import path

from apps.accounts.views.auth import RegisterAPIView
from apps.accounts.views.auth import LoginAPIView
app_name = "accounts_api"

urlpatterns = [

    path(
        "register/",
        RegisterAPIView.as_view(),
        name="api-register"
    ),
path(
    "login/",
    LoginAPIView.as_view(),
    name="api-login",
),



]