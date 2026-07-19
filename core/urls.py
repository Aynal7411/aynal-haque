from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path("", views.homepage_redesign, name="homepage_redesign"), 
    path('skills/', views.skills_view, name='skills'),
    path("legacy/", views.my_page, name="home-page"),
   
    path(
        "projects/",
        views.project_list,
        name="project_list",
    ),

    path(
        "projects/<slug:slug>/",
        views.project_detail,
        name="project_detail",
    ),

    path("about/", views.about_us, name="about"),
    path('privacy-policy/', views.privacy_policy, name="privacy_policy"),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('expertise/', views.expertise_view, name='expertise'),
    # Password Reset URLs
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

