from django.db import models

from apps.ingredient.models import Spice, Meat, Vegetable, Cheese, Sauce, Tag


class Pasta(models.Model):
    name = models.CharField(max_length=100)
    front_description = models.TextField()
    front_image = models.ImageField(upload_to='pastas/front/')
    details_description = models.TextField()
    details_image = models.ImageField(upload_to='pastas/details/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    spices = models.ManyToManyField(Spice, blank=True)
    meats = models.ManyToManyField(Meat, blank=True)
    vegetables = models.ManyToManyField(Vegetable, blank=True)
    cheese = models.ManyToManyField(Cheese, blank=True)
    sauce = models.ManyToManyField(Sauce, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name
