from django.core.management.base import BaseCommand

from apps.chicken.models import Chicken


class Command(BaseCommand):
    help = "Populate the Chicken model with initial data."

    def handle(self, *args, **kwargs):
        chickens = [
            {
                "product_name": "ПИЛЕ КИКЕРС",
                "product_picture": "chicken/807ipar.png",
                "ingredient": "Късчета от сочни пикантни пилешки гърди, с хрупкава обвивка, изпечени на фурна придружени със сос Барбекю",
                "price": 7.9,
                "tag": {"SPICY": "https://www.dominos.bg/images/tags/spicy.svg"},
            },
            {
                "product_name": "ПИЛЕ СТРИПЕРС",
                "product_picture": "chicken/811ipar.png",
                "ingredient": "Сочни филенца от пилешки гърди, не пикантни, с хрупкава обвивка, изпечени на фурна, придружени със сладко лютив сос",
                "price": 7.9,
                "tag": {},
            },
            {
                "product_name": "КРИЛЦА Buffalo",
                "product_picture": "chicken/809ipar.png",
                "ingredient": "8 прясно изпечени пилешки крилца със сос Барбекю",
                "price": 7.9,
                "tag": {},
            },
            {
                "product_name": "Крилца Buffalo люти",
                "product_picture": "chicken/718ipar.png",
                "ingredient": "8 прясно изпечени пилешки крилца в лют сос Franks",
                "price": 7.9,
                "tag": {"SPICY": "https://www.dominos.bg/images/tags/spicy.svg"},
            },
        ]

        for data in chickens:
            item = Chicken.objects.create(
                name=data["product_name"],
                description=data["ingredient"],
                image=data["product_picture"],
                price=data["price"],
            )
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created DoughType: {item}")
            )
