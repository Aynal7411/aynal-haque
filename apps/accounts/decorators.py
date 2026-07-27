from django.shortcuts import redirect


def role_required(role):

    def decorator(view_func):

        def wrapper(request, *args, **kwargs):

            user = request.user

            if not user.is_authenticated:
                return redirect("login")


            if user.profile.role != role:
                return redirect("home")


            return view_func(
                request,
                *args,
                **kwargs
            )


        return wrapper

    return decorator