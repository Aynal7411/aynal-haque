from django.contrib import messages
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.forms.login_form import LoginForm
from apps.accounts.forms.registration_form import RegistrationForm

from apps.accounts.services.auth_service import (
    authenticate_user,
    generate_tokens,
    logout_user,
    register_user,
)



def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            register_user(
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            messages.success(request, "Account created successfully. Please sign in.")
            return redirect("accounts:login")
    else:
        form = RegistrationForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate_user(
                request,
                form.cleaned_data["email"],
                form.cleaned_data["password"],
            )
            if user is not None:
                return redirect("website:home")
            messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout_user(request)
    return redirect("accounts:login")