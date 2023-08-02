from django.contrib import admin

from apps.chicken.models import Chicken
from apps.ingredient.admin import TagAdmin

# Register your models here.
admin.site.register(Chicken, TagAdmin)