from django.shortcuts import render,redirect, get_object_or_404
from .models import Profile
from datetime import datetime
from django.contrib.auth.models import User
# Create your views here.
from .models import Post,SiteAlert
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def my_page(request):
    alert = SiteAlert.objects.filter(is_active=True).order_by('-created_on').first()
    profile = Profile.objects.first()  # Get first instance instead of 404
    if not profile:
        return render(request, 'no_profile.html')  # Create this template
    return render(request, 'home_page.html', {
         'alert': alert,
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

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)  # optional: auto login after registration
            return redirect('home-page')

    return render(request, 'register.html')
   
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home-page')  


def project_view(request):
    return render(request, 'project.html')

def about_us(request):
        return render(request, 'about.html')

def home_view(request):
    return render(request, 'home.html')