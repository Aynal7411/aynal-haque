from django.urls import path

from . import views


app_name = "website"

urlpatterns = [

    path(
        "",
        views.home_view,
        name="home",
    ),

    path(
        "about/",
        views.about_view,
        name="about",
    ),

    path(
        "expertise/",
        views.expertise_view,
        name="expertise",
    ),

    path(
        "projects/",
        views.projects_view,
        name="projects",
    ),

    path(
        "contact/",
        views.contact_view,
        name="contact",
    ),

]