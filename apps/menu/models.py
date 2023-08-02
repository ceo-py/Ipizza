from django.db import models

from apps.ingredient.models import Tag


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name
