from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TeamMemberForm
from .models import Post, Profile, Project, SiteAlert, Skill


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
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            messages.error(request, 'Please provide both username and password.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! Your account has been created.')
            return redirect('home-page')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home-page')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home-page')


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
