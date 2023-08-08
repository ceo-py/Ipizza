from django.core.management.base import BaseCommand

from apps.appetizer.models import Appetizer


class Command(BaseCommand):
    help = "Populate the Appetizer model with initial data."

    def handle(self, *args, **kwargs):
        Appetizers = [
            {
                "product_name": "Моцарелено хлебче",
                "product_picture": "appetizers/1333ipar.png",
                "ingredient": "Прясно изпечено пухкаво хлебче с моцарела и специалната подправка на Доминос, придружено с доматен сос",
                "price": 4.5,
                "tag": {
                    "VEGETARIAN": "https://www.dominos.bg/images/tags/vegetarian.svg"
                },
            },
            {
                "product_name": "Картофки Уеджис",
                "product_picture": "appetizers/1231ipar.png",
                "ingredient": "Запечени на фурна картофки с апетитна коричка, леко подправени, придружени със сос Барбекю",
                "price": 4.5,
                "tag": {
                    "VEGETARIAN": "https://www.dominos.bg/images/tags/vegetarian.svg"
                },
            },
            {
                "product_name": "Моцарелени пръчици",
                "product_picture": "appetizers/1230ipar.png",
                "ingredient": "5 броя хрупкави моцарелени пръчици със сос барбекю",
                "price": 7.5,
                "tag": {},
            },
        ]

        for data in Appetizers:
            item = Appetizer.objects.create(
                name=data["product_name"],
                description=data["ingredient"],
                image=data["product_picture"],
                price=data["price"],
            )
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created Appetizer: {item}")
            )
