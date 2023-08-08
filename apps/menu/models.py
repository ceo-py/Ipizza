from django.core import validators
from django.db import models

from apps.ingredient.models import Tag


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=(validators.MinValueValidator(0),)
    )
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name
