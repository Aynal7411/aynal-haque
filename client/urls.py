from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_business, name='register_business'),
     path('dashboard/', views.dashboard, name='dashboard'),
    
]
