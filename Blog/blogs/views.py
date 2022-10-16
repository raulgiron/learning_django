# System Imports
from django.shortcuts import render

# My Imports
from .models import BlogPost


# Create your views here.
def index(request):
    """The home page for Blogs App"""
    return render(request, 'blogs/index.html')
