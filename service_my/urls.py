from .views import services_view
from django.urls import path
urlpatterns = [
    path('', services_view, name='services-page'),
]
