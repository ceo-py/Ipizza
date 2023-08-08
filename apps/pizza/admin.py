from django.contrib import admin
from apps.pizza.models import Pizza


# Register the PizzaAdmin class
class MainMenuAdmin(admin.ModelAdmin):
    ordering = ("name", "price")
    list_filter = ("tags",)
    list_display = ("name", "description", "price")
    filter_horizontal = ("spices", "meats", "vegetables", "cheese", "sauce", "tags")
    list_per_page = 15

    def description(self, obj):
        products = obj.front_description
        return products

    description.short_description = "Description"


# Register the Pizza model with the custom admin class
admin.site.register(Pizza, MainMenuAdmin)
