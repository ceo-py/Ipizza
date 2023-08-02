from django.contrib import admin

from apps.ingredient.admin import TagAdmin
from apps.sauce.models import SauceMenu

# Register your models here.

admin.site.register(SauceMenu, TagAdmin)
