from django.contrib import messages
from django.shortcuts import redirect, render

from apps.contact.forms import ContactForm


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(
                request,
                "Thanks for reaching out. I will get back to you soon.",
            )
            return redirect("contact:contact")
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})
