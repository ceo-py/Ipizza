from django.db import models
from apps.menu.models import Menu


# Create your models here.
class Desert(Menu):
    image = models.ImageField(upload_to='desert/')

