from django.contrib import admin

from apps.desert.models import Desert
from apps.ingredient.admin import TagAdmin

# Register your models here.
admin.site.register(Desert, TagAdmin)