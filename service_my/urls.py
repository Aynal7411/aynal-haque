from .views import services_view,contact_view
from django.urls import path
urlpatterns = [
    path('', services_view, name='services-page'),
     path('contact/', contact_view, name='contact'),
]
