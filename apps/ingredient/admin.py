from django.contrib import admin

from apps.ingredient.models import Spice, Meat, Vegetable, Cheese, Sauce, Tag


class TagAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    search_fields = ('description', 'name')
    list_display = ('name', 'description', 'price')


# Register your models here.
# Register the ingredient models
admin.site.register(Spice)
admin.site.register(Meat)
admin.site.register(Vegetable)
admin.site.register(Cheese)
admin.site.register(Sauce)
admin.site.register(Tag)
