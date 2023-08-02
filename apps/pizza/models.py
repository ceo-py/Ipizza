from django.db import models

from apps.dough_types.models import DoughType
from apps.ingredients.models import Spice, Meat, Vegetable, Cheese, Sauce, Tag


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    front_description = models.TextField()
    front_image = models.ImageField(upload_to='pizzas/front/')
    details_description = models.TextField()
    details_image = models.ImageField(upload_to='pizzas/details/')
    dough_type = models.ForeignKey(DoughType, on_delete=models.SET_NULL, null=True)
    spices = models.ManyToManyField(Spice, blank=True)
    meats = models.ManyToManyField(Meat, blank=True)
    vegetables = models.ManyToManyField(Vegetable, blank=True)
    cheese = models.ManyToManyField(Cheese, blank=True)
    sauce = models.ManyToManyField(Sauce, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name
