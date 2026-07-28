from django.contrib import messages
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from apps.contact.forms import ContactForm





def home_view(request):
    return render(request, "website/home.html")


def about_view(request):
    return render(request, "website/about.html")


def expertise_view(request):
    return render(request, "website/expertise.html")


def projects_view(request):
    return render(request, "website/projects.html")


@require_http_methods(["GET", "POST"])
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(
                request,
                "Thanks for reaching out. I will get back to you shortly.",
            )
            form = ContactForm()
        else:
            messages.error(request, "Please correct the highlighted fields.")
    else:
        form = ContactForm()

    return render(request, "website/contact.html", {"form": form})


