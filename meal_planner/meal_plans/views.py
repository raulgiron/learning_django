# System Imports
from django.shortcuts import render

# My Imports
from .models import Day

# Create your views here.
def index(request):
    """The home page for Meal Planner."""
    return render(request, 'meal_plans/index.html')

def days(request):
    """Show all days of the week."""
    days = Day.objects.order_by('date_added')
    context = {'days': days}
    return render(request, 'meal_plans/days.html', context)

def day(request, day_id):
    """Show a single day and all its meals."""
    day = Day.objects.get(id=day_id)
    meals = day.meal_set.order_by('date_added')
    context = {'day': day, 'meals': meals}
    return render(request, 'meal_plans/day.html', context)