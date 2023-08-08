from django.core.management.base import BaseCommand
from apps.sauce.models import SauceMenu


class Command(BaseCommand):
    help = "Populate the Sauce model with initial data."

    def handle(self, *args, **kwargs):
        sauces = [
            {
                "product_name": "Медена Горчица",
                "product_picture": "sauce/1366ipar.png",
                "ingredients": "",
                "price": 1.0,
                "tag": {},
            },
            {
                "product_name": "Чеснов coc",
                "product_picture": "sauce/1201ipar.png",
                "ingredients": "",
                "price": 1.0,
                "tag": {},
            },
            {
                "product_name": "Барбекю сос",
                "product_picture": "sauce/1200ipar.png",
                "ingredients": "",
                "price": 1.0,
                "tag": {},
            },
            {
                "product_name": "Чили сос",
                "product_picture": "sauce/1202ipar.png",
                "ingredients": "",
                "price": 1.0,
                "tag": {},
            },
            {
                "product_name": "Доматен сос",
                "product_picture": "sauce/1206ipar.png",
                "ingredients": "",
                "price": 1.0,
                "tag": {},
            },
            {
                "product_name": "Млечен сос",
                "product_picture": "sauce/1207ipar.png",
                "ingredients": "",
                "price": 1.0,
                "tag": {},
            },
            {
                "product_name": "Ранч сос",
                "product_picture": "sauce/1205ipar.png",
                "ingredients": "",
                "price": 1.0,
                "tag": {},
            },
            {
                "product_name": "Цезар сос",
                "product_picture": "sauce/1512ipar.png",
                "ingredients": "Цезар сос",
                "price": 1.0,
                "tag": {},
            },
            {
                "product_name": "Балсамов дресинг",
                "product_picture": "sauce/1646ipar.png",
                "ingredients": "Балсамов дресинг",
                "price": 1.0,
                "tag": {},
            },
        ]

        for data in sauces:
            item = SauceMenu.objects.create(
                name=data["product_name"],
                description=data["ingredients"],
                image=data["product_picture"],
                price=data["price"],
            )
            self.stdout.write(self.style.SUCCESS(f"Successfully created Sauce: {item}"))
