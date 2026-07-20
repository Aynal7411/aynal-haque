from django.shortcuts import render,redirect
from django.contrib import messages as django_messages
from .forms import ClientContactForm
# Create your views here.
from .models import Service

def services_view(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def get_client_ip(request):

    x_forwarded_for = request.META.get(
        "HTTP_X_FORWARDED_FOR"
    )

    if x_forwarded_for:

        ip = x_forwarded_for.split(",")[0]

    else:

        ip = request.META.get(
            "REMOTE_ADDR"
        )

    return ip

def contact_view(request):
    if request.method == 'POST':
        form = ClientContactForm(request.POST)
        if form.is_valid():
            contact = form.save(
                commit=False
            )
           
            contact.ip_address = (
                get_client_ip(request)
            )
            contact.save()
            django_messages.success(request, 'Your message has been sent successfully!')
            return redirect('homepage_redesign')  # Redirect to a success page or any other page
    else:
        form = ClientContactForm()
    return render(request, 'contact.html', {'form': form})   


def process_view(request):
    return render(request, 'process.html')
