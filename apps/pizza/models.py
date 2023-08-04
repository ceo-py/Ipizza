from django.db import models
from django.core import validators
from apps.dough_type.models import DoughType
from apps.ingredient.models import Spice, Meat, Vegetable, Cheese, Sauce, Tag
from custom_validations.cv import CustomValidation as CV


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    front_description = models.TextField(max_length=500)
    front_image = models.ImageField(
        upload_to='pizzas/front/',
        validators=(CV.validate_image_size,))
    details_description = models.TextField(max_length=500)
    details_image = models.ImageField(
        upload_to='pizzas/details/',
        validators=(CV.validate_image_size,)
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=(
            validators.MinValueValidator(0),
        ))
    dough_type = models.ForeignKey(DoughType, on_delete=models.SET_NULL, null=True)
    spices = models.ManyToManyField(Spice, blank=True)
    meats = models.ManyToManyField(Meat, blank=True)
    vegetables = models.ManyToManyField(Vegetable, blank=True)
    cheese = models.ManyToManyField(Cheese, blank=True)
    sauce = models.ManyToManyField(Sauce, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name
