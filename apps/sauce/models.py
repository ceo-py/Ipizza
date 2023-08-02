from django.db import models

from apps.menu.models import Menu


# Create your models here.
class SauceMenu(Menu):
    image = models.ImageField(upload_to='sauce/')
