from django.db import models

from apps.ingredient.models import Spice, Meat, Vegetable, Cheese, Sauce
from apps.menu.models import Menu


# Create your models here.
class Sandwich(Menu):
    image = models.ImageField(upload_to='sandwich/')
    spices = models.ManyToManyField(Spice, blank=True)
    meats = models.ManyToManyField(Meat, blank=True)
    vegetables = models.ManyToManyField(Vegetable, blank=True)
    cheese = models.ManyToManyField(Cheese, blank=True)
    sauce = models.ManyToManyField(Sauce, blank=True)
