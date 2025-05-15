from django.shortcuts import render

# Create your views here.
from .models import Service

def services_view(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})
