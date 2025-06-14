from django.urls import path
from hello.views import webhook

urlpatterns = [
    path("webhook", webhook, name="webhook"),
]
