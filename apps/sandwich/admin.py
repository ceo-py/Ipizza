from django.contrib import admin

from apps.pizza.admin import MainMenuAdmin
from apps.sandwich.models import Sandwich

# Register your models here.
admin.site.register(Sandwich, MainMenuAdmin)
