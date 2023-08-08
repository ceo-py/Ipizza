from django.contrib import admin

from apps.pasta.models import Pasta
from apps.pizza.admin import MainMenuAdmin

# Register your models here.

admin.site.register(Pasta, MainMenuAdmin)
