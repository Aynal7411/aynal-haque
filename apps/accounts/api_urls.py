from django.urls import path

from apps.accounts.views.auth import RegisterAPIView


urlpatterns = [

    path(
        "register/",
        RegisterAPIView.as_view(),
        name="api-register"
    ),

]