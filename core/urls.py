from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('register/',views.register_view, name='register'),
    path('login/',views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('skills/', views.skills_view, name='skills'),
    path("", views.my_page, name="home-page"),
    path("project/" ,views.project_view, name="project_list"),
    path("about/", views.about_us, name="about"),
    path('homepage/', views.home_view, name="home_page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
