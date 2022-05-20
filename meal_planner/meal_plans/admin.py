from django.contrib import admin

# Register your imports here.
from .models import Day
from .models import Meal


# Register your models here.
admin.site.register(Day)
admin.site.register(Meal)