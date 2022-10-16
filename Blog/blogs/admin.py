from django.contrib import admin


# Register your imports here.
from .models import BlogPost

# Register your models here.
admin.site.register(BlogPost)
