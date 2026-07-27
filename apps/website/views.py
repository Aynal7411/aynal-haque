from django.shortcuts import render


def home_view(request):

    return render(
        request,
        "website/home.html",
    )


def about_view(request):

    return render(
        request,
        "website/about.html",
    )


def expertise_view(request):

    return render(
        request,
        "website/expertise.html",
    )


def projects_view(request):

    return render(
        request,
        "website/projects.html",
    )


def contact_view(request):

    return render(
        request,
        "website/contact.html",
    )