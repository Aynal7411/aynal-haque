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
from django.shortcuts import render
from .models import Skill

def skills_view(request):
    skill_types = Skill.SKILL_TYPES
    grouped_skills = {}

    for key, label in skill_types:
        grouped_skills[label] = Skill.objects.filter(skill_type=key).order_by('-percentage')

    return render(request, 'skills.html', {'grouped_skills': grouped_skills})



   
  