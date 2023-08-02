from django.contrib import admin
from apps.pizza.admin import MainMenuAdmin
from apps.salad.models import Salad

# Register your models here.

admin.site.register(Salad, MainMenuAdmin)