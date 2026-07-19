from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import  UserRegistrationForm, UserProfileForm, UserPasswordChangeForm
from .models import  Profile, Project, Skill, UserProfile

from core.services.home_page_service import build_home_page_context


def homepage_redesign(request):
    """
    Premium redesigned homepage for Aynal's Solutions
    Backend Engineering with Python, Django, DRF, and PostgreSQL
    """
    context = {
        'title': "Aynal's Solutions - Backend Engineering with Python & Django",
        'description': 'Building secure, scalable, and maintainable backend systems using Python, Django, DRF, and PostgreSQL',
    }
    return render(request, 'homepage_redesign.html', context)


def my_page(request):
    context = build_home_page_context()

    if context["profile"] is None:
        return render(
            request,
            "no_profile.html",
            status=200,
        )

    return render(
        request,
        "home_page.html",
        context,
    )


def skills_view(request):
    skill_types = Skill.SKILL_TYPES
    grouped_skills = {
        label: Skill.objects.filter(skill_type=key).order_by('-percentage')
        for key, label in skill_types
    }
    return render(request, 'skills.html', {'grouped_skills': grouped_skills})



#User registration system

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home-page')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
            )

            if user is not None:
                login(request, user)

                messages.success(
                    request,
                    f"Welcome, {user.username}! Your account has been created."
                )

                return redirect('profile')

            messages.error(request, "Authentication failed after registration.")

        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    else:
        form = UserRegistrationForm()

    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home-page')


@login_required(login_url='login')
def profile_view(request):
    """Display user profile"""
    user_profile = get_object_or_404(UserProfile, user=request.user)
    context = {
        'user_profile': user_profile,
        'user': request.user,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def profile_edit(request):
    """Edit user profile"""
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = UserProfileForm(instance=user_profile, user=request.user)

    context = {
        'form': form,
        'user_profile': user_profile,
    }
    return render(request, 'profile_edit.html', context)


@login_required(login_url='login')
def password_change_view(request):
    """Change user password"""
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password1')
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Your password has been changed successfully.')
            return redirect('profile')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = UserPasswordChangeForm(request.user)

    context = {'form': form}
    return render(request, 'password_change.html', context)


@login_required(login_url='login')
def profile_delete_confirm(request):
    """Confirm user account deletion"""
    if request.method == 'POST':
        user = request.user
        username = user.username
        logout(request)
        user.delete()
        messages.success(request, f'Account "{username}" has been deleted successfully.')
        return redirect('home-page')
    
    return render(request, 'profile_delete_confirm.html')


from django.shortcuts import render, get_object_or_404

from .models import Project


def project_list(request):

    projects = (
        Project.objects
        .select_related("category")
        .prefetch_related("technologies")
        .filter(status="completed")
        .order_by("order")
    )

    context = {
        "projects": projects
    }

    return render(
        request,
        "project_list.html",
        context,
    )


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

#About Us Page
def about_us(request):
     profile = Profile.objects.first()  # Assuming there's only one profile for the company
     skills= Skill.objects.order_by('name')  # Fetch all skills
     context = {
         'profile': profile,
         'skills': skills,
     }
     return render(request, 'about.html', context)


def privacy_policy(request):
    return render(request, 'privacy_policy.html')




def thank_you(request):
    return render(request, 'thank_you.html')

def expertise_view(request):
    return render(request, 'expertise.html')


