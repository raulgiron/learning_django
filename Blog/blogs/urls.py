"""Defines URL patterns for Blog Posts APP."""

# System Imports
from django.urls import path

# My Imports
from . import views


app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]
