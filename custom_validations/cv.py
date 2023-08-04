from django.core.exceptions import ValidationError


class CustomValidation:

    @staticmethod
    def validate_image_size(value):
        max_size = 1 * 1024 * 1024

        if value.size > max_size:
            raise ValidationError(f"The image size should not exceed {max_size / (1024 * 1024)} MB.")

