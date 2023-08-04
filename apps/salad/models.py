from django.db import models

from apps.ingredient.models import Spice, Meat, Vegetable, Cheese, Sauce, Tag
from apps.menu.models import Menu
from custom_validations.cv import CustomValidation as CV


# Create your models here.
class Salad(Menu):
    image = models.ImageField(upload_to='salads/',validators=(CV.validate_image_size,))
    spices = models.ManyToManyField(Spice, blank=True)
    meats = models.ManyToManyField(Meat, blank=True)
    vegetables = models.ManyToManyField(Vegetable, blank=True)
    cheese = models.ManyToManyField(Cheese, blank=True)
    sauce = models.ManyToManyField(Sauce, blank=True)


