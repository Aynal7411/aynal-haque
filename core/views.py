from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TeamMemberForm, UserRegistrationForm, UserProfileForm, UserPasswordChangeForm
from .models import Post, Profile, Project, SiteAlert, Skill, UserProfile


def my_page(request):
    alert = SiteAlert.objects.filter(is_active=True).order_by('-created_on').first()
    profile = Profile.objects.first()
    if not profile:
        return render(request, 'no_profile.html')

    return render(request, 'home_page.html', {
        'alert': alert,
        'profile': profile,
        'year': datetime.now().year,
    })


def skills_view(request):
    skill_types = Skill.SKILL_TYPES
    grouped_skills = {
        label: Skill.objects.filter(skill_type=key).order_by('-percentage')
        for key, label in skill_types
    }
    return render(request, 'skills.html', {'grouped_skills': grouped_skills})


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! Your account has been created.')
            return redirect('profile')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


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


def project_view(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'project.html', {'projects': projects})


def about_us(request):
    return render(request, 'about.html')


def home_view(request):
    return render(request, 'home.html')


def join_team(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your request to join the team has been submitted.')
            return redirect('thank_you')
    else:
        form = TeamMemberForm()

    return render(request, 'join_team.html', {'form': form})


def thank_you(request):
    return render(request, 'thank_you.html')

