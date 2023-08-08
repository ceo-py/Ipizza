from django.contrib import admin

from apps.appetizer.models import Appetizer
from apps.ingredient.admin import TagAdmin

# Register your models here.

admin.site.register(Appetizer, TagAdmin)
