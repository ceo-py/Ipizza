from django.db import models

from apps.dough_types.models import DoughType
from apps.ingredients.models import Spice, Meat, Vegetable, Cheese, Sauce, Tag


class Chicken(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='chicken/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name
