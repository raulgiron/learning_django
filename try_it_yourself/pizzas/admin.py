from django.contrib import admin

# Register your imports here.
from .models import Pizza
from .models import Topping


# Register your models here.
admin.site.register(Pizza)
admin.site.register(Topping)