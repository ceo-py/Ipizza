from django.db import models

from apps.menu.models import Menu


# Create your models here.
class Drink(Menu):
    image = models.ImageField(upload_to='drinks/')
