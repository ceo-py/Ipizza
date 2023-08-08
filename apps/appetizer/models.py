from django.db import models

from apps.menu.models import Menu
from custom_validations.cv import CustomValidation as CV


# Create your models here.
class Appetizer(Menu):
    image = models.ImageField(
        upload_to="appetizers/", validators=(CV.validate_image_size,)
    )
