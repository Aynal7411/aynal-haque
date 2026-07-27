from django.urls import path
from apps.accounts.views.auth import (
    register_view,
    login_view,
    logout_view,
)

app_name = "apps.accounts"

urlpatterns = [
     

    path(
        "register/",
        register_view,
        name="register"
    ),

    path(
        "login/",
        login_view,
        name="login"
    ),

    path(
        "logout/",
        logout_view,
        name="logout"
    ),


]