from django.contrib import admin

from apps.pizza.models import Pizza


# Register the PizzaAdmin class
class PizzaAdmin(admin.ModelAdmin):
    filter_horizontal = ('spices', 'meats', 'vegetables', 'cheese', 'sauce')


# Register the Pizza model with the custom admin class
admin.site.register(Pizza, PizzaAdmin)
