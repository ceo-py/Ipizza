from django.core.management.base import BaseCommand

from apps.drink.models import Drink


class Command(BaseCommand):
    help = 'Populate the Drink model with initial data.'

    def handle(self, *args, **kwargs):
        drinks = [
            {
                "product_name": "Айрян 0.5L",
                "product_picture": "drinks/1503ipar.png",
                "ingredients": "",
                "price": 2.6,
                "tag": {}
            },
            {
                "product_name": "Red Bull 250ml",
                "product_picture": "drinks/1659ipar.png",
                "ingredients": "",
                "price": 3.7,
                "tag": {
                    "НОВО": "https://www.dominos.bg/images/tags/new_product.svg"
                }
            },
            {
                "product_name": "Red Bull Sugarfree 250ml",
                "product_picture": "drinks/1660ipar.png",
                "ingredients": "",
                "price": 3.7,
                "tag": {
                    "НОВО": "https://www.dominos.bg/images/tags/new_product.svg"
                }
            },
            {
                "product_name": "Coca-Cola Zero",
                "product_picture": "drinks/1638ipar.png",
                "ingredients": "",
                "price": 2.6,
                "tag": {}
            },
            {
                "product_name": "Coca-Cola",
                "product_picture": "drinks/1603ipar.png",
                "ingredients": "",
                "price": 2.6,
                "tag": {}
            },
            {
                "product_name": "Минерална вода",
                "product_picture": "drinks/1637ipar.png",
                "ingredients": "",
                "price": 2.0,
                "tag": {}
            },
            {
                "product_name": "FANTA",
                "product_picture": "drinks/1639ipar.png",
                "ingredients": "",
                "price": 2.6,
                "tag": {}
            },
            {
                "product_name": "Cappy Pulpy",
                "product_picture": "drinks/1636ipar.png",
                "ingredients": "",
                "price": 2.4,
                "tag": {}
            },
            {
                "product_name": "Fuzztea",
                "product_picture": "drinks/1641ipar.png",
                "ingredients": "",
                "price": 2.5,
                "tag": {}
            },
            {
                "product_name": "Carlsberg 0.5L",
                "product_picture": "drinks/1632ipar.png",
                "ingredients": "",
                "price": 3.2,
                "tag": {}
            },
            {
                "product_name": "Шуменско 0.5L",
                "product_picture": "drinks/1628ipar.png",
                "ingredients": "",
                "price": 2.4,
                "tag": {}
            },
            {
                "product_name": "Шуменско 1л",
                "product_picture": "drinks/1627ipar.png",
                "ingredients": "",
                "price": 2.8,
                "tag": {}
            }
        ]

        for data in drinks:
            item = Drink.objects.create(
                name=data['product_name'],
                description=data['ingredients'],
                image=data['product_picture'],
                price=data['price'],
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Drink: {item}'))
