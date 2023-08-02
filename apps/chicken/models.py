from django.db import models
from apps.menu.models import Menu


class Chicken(Menu):
    image = models.ImageField(upload_to='chicken/')
