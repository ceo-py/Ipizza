from django.contrib import admin

from apps.ingredients.models import Spice, Meat, Vegetable, Cheese, Sauce

# Register your models here.
# Register the ingredient models
admin.site.register(Spice)
admin.site.register(Meat)
admin.site.register(Vegetable)
admin.site.register(Cheese)
admin.site.register(Sauce)
