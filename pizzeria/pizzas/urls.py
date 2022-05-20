"""Defines URL patterns for pizzas APP."""

# System Imports
from django.urls import path

# My Imports
from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all days of the week
    path('pizzas/', views.pizzas, name='pizzas'),
    # Detail page for a single pizza
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]