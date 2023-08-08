from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from custom_validations.cv import CustomValidation as CV


def validate_pick(value):
    allowed_picks = {x for items in DoughType.DOUGH_SIZES for x in items}
    if value not in allowed_picks:
        raise ValidationError(
            "Invalid pick value. Please choose from the available options."
        )


class DoughType(models.Model):
    DOUGH_SIZES = (
        ("Средна", "Средна"),
        ("Голяма", "Голяма"),
        ("Джъмбо", "Джъмбо"),
    )

    type = models.CharField(
        max_length=100, choices=DOUGH_SIZES, validators=(validate_pick,)
    )
    picture = models.ImageField(
        upload_to="dough/", validators=(CV.validate_image_size,)
    )
    description = models.TextField(max_length=500)
    price = models.DecimalField(
        decimal_places=2, max_digits=6, validators=(validators.MinValueValidator(0),)
    )

    def __str__(self):
        return f"{self.type} - {self.description}"
