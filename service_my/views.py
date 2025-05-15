from django.shortcuts import render,redirect
from django.contrib import messages as django_messages
from .forms import MessageForm
# Create your views here.
from .models import Service

def services_view(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def contact_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            django_messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = MessageForm()
    return render(request, 'contact.html', {'form': form})   
