from django.core.exceptions import ValidationError


class CustomValidation:
    @staticmethod
    def validate_image_size(value):
        max_size = 5 * 1024 * 1024

        if value.size > max_size:
            raise ValidationError(
                f"The image size should not exceed {max_size / (1024 * 1024)} MB."
            )

    @staticmethod
    def is_not_logged_in(user):
        return not user.is_authenticated

    @staticmethod
    def logged_in(user):
        return user.is_authenticated

    @staticmethod
    def validate_only_letters(value):
        if not value.isalpha():
            raise ValidationError("The name should contain only letters.")
