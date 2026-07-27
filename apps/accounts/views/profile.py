from django.contrib.auth.decorators import login_required

from django.contrib.auth import update_session_auth_hash

from django.shortcuts import render

from django.shortcuts import redirect

from apps.accounts.forms.profile_form import (
    ProfileForm,
)

from apps.accounts.forms.password_form import (
    UserPasswordChangeForm,
)

from apps.accounts.selectors.profile_selector import (
    get_profile,
)

from apps.accounts.services.profile_service import (
    update_profile,
)


@login_required
def profile_view(request):

    profile = get_profile(request.user)

    return render(
        request,
        "accounts/profile.html",
        {
            "profile": profile,
        },
    )


@login_required
def edit_profile_view(request):

    profile = get_profile(request.user)

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )

        if form.is_valid():

            update_profile(
                profile,
                form,
            )

            return redirect(
                "accounts:profile"
            )

    else:

        form = ProfileForm(
            instance=profile
        )

    return render(
        request,
        "accounts/edit_profile.html",
        {
            "form": form,
        },
    )


@login_required
def change_password_view(request):

    if request.method == "POST":

        form = UserPasswordChangeForm(
            request.user,
            request.POST,
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(
                request,
                user,
            )

            return redirect(
                "accounts:profile"
            )

    else:

        form = UserPasswordChangeForm(
            request.user,
        )

    return render(
        request,
        "accounts/change_password.html",
        {
            "form": form,
        },
    )