from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from.models import ProjectStatus

from .models import  Project, Skill




def homepage_redesign(request):
    """
    Premium redesigned homepage for Aynal's Solutions
    Backend Engineering with Python, Django, DRF, and PostgreSQL
    """
    context = {
        'title': "Aynal's Solutions - Backend Engineering with Python & Django",
        'description': 'Building secure, scalable, and maintainable backend systems using Python, Django, DRF, and PostgreSQL',
    }
    return render(request, 'core/homepage_redesign.html', context)



def skills_view(request):
    skill_types = Skill.SKILL_TYPES
    grouped_skills = {
        label: Skill.objects.filter(skill_type=key).order_by('-percentage')
        for key, label in skill_types
    }
    return render(request, 'skills.html', {'grouped_skills': grouped_skills})



#User registration system


from django.shortcuts import render, get_object_or_404

from .models import Project

def project_list(request):
    projects = (
        Project.objects
        .select_related("category")
        .prefetch_related("technologies")
        .filter(status=ProjectStatus.COMPLETED)
        .order_by("order")
    )

    context = {
        "projects": projects,
    }

    return render(request, "project_list.html", context)

def project_detail(request, slug):

    project = get_object_or_404(
        Project.objects
        .select_related("category")
        .prefetch_related(
            "technologies",
            "images",
            "features",
        ),
        slug=slug,
    )

    context = {
        "project": project
    }

    return render(
        request,
        "project_detail.html",
        context,
    )

def about_us(request):
   

    return render(request, "about.html")


def privacy_policy(request):
    return render(request, 'privacy_policy.html')




def thank_you(request):
    return render(request, 'thank_you.html')

def expertise_view(request):
    return render(request, 'expertise.html')


