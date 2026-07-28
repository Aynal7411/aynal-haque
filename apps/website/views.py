
from django.shortcuts import render

def home_view(request):
    return render(request, "website/home.html")


def about_view(request):
    return render(request, "website/about.html")


def expertise_view(request):
    return render(request, "website/expertise.html")

