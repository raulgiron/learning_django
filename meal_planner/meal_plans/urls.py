"""Defines URL patterns for learning_logs APP."""

#System Imports
from django.urls import path

#My Imports
from . import views


app_name = 'meal_plans'
urlpatterns = [
        # Home page
        path('', views.index, name='index'),
        # Page that shows all days of the week
        path('days/', views.days, name='days'),
        # Detail page for a single day
        path('days/<int:day_id>/', views.day, name='day'),
        ]
