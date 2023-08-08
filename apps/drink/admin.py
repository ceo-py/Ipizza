from django.contrib import admin

from apps.drink.models import Drink
from apps.ingredient.admin import TagAdmin

# Register your models here.
admin.site.register(Drink, TagAdmin)
