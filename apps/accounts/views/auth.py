from django.shortcuts import render, redirect
from rest_framework.views import APIView
from apps.accounts.forms.login_form import LoginForm
from apps.accounts.forms.registration_form import RegistrationForm
from rest_framework.response import Response
from rest_framework import status
from apps.accounts.services.auth_service import (
    register_user,
    authenticate_user,
    logout_user,
)


from apps.accounts.serializers import RegisterSerializer


class RegisterAPIView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = serializer.save()

        return Response(
            {
                "message": "User created successfully",
                "email": user.email
            },
            status=status.HTTP_201_CREATED
        )


def register_view(request):

    if request.method == "POST":

        form = RegistrationForm(request.POST)

        if form.is_valid():

            user = register_user(
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )

            return redirect("login")


    else:
        form = RegistrationForm()


    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )



def login_view(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            user = authenticate_user(
                request,
                form.cleaned_data["email"],
                form.cleaned_data["password"]
            )

            if user:
                return redirect("home")


    else:
        form = LoginForm()


    return render(
        request,
        "accounts/login.html",
        {
            "form": form
        }
    )



def logout_view(request):

    logout_user(request)

    return redirect("login")