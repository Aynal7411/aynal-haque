from django.shortcuts import render, get_object_or_404
from .models import Profile
from datetime import datetime
# Create your views here.

def my_page(request):
    
    profile = Profile.objects.first()  # Get first instance instead of 404
    if not profile:
        return render(request, 'no_profile.html')  # Create this template
    return render(request, 'home_page.html', {
        'profile': profile,
        'year': datetime.now().year
    })




   
  