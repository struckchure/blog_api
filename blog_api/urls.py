"""blog_api URL Configuration
"""
from django.urls import path, include

urlpatterns = [
    path("api/v1/", include("core.urls")),
]
