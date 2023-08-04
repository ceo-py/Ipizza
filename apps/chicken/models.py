from django.db import models
from apps.menu.models import Menu
from custom_validations.cv import CustomValidation as CV


class Chicken(Menu):
    image = models.ImageField(
        upload_to='chicken/',
        validators=(CV.validate_image_size,))
