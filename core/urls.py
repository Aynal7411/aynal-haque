from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('post', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/change-password/', views.password_change_view, name='password_change'),
    path('profile/delete/', views.profile_delete_confirm, name='profile_delete'),
    path('skills/', views.skills_view, name='skills'),
    path("", views.my_page, name="home-page"),
    path("project/", views.project_view, name="project_list"),
    path("about/", views.about_us, name="about"),
    path('privacy-policy/', views.privacy_policy, name="privacy_policy"),
    path('join/', views.join_team, name='join_team'),
    path('thank-you/', views.thank_you, name='thank_you'),

    # Password Reset URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt',
        success_url='/password-reset/done/'
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html',
        success_url='/password-reset-complete/'
    ), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

