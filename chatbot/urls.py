from django.urls import path
from .views import chat_view
from django.views.generic import TemplateView

urlpatterns = [
    path("ask/", chat_view, name="chatbot"),
    path("", TemplateView.as_view(template_name="chat.html"), name="chat-page"),
]
