from django.core.management.base import BaseCommand

from apps.desert.models import Desert


class Command(BaseCommand):
    help = 'Populate the Desert model with initial data.'

    def handle(self, *args, **kwargs):
        deserts = [
            {
                "product_name": "Чоко пай",
                "product_picture": "deserts/1204ipar.png",
                "ingredient": "Пухкав десерт с пълнеж NUTELLA, прясно изпечен на фурна и поръсен с пудра захар",
                "price": 6.9,
                "tag": {}
            },
            {
                "product_name": "Шоколадово суфле",
                "product_picture": "deserts/1228ipar.png",
                "ingredient": "Топло шоколадово кексче с пълнеж от разтопен шоколад",
                "price": 5.9,
                "tag": {}
            },
            {
                "product_name": "Брaуни хапки",
                "product_picture": "deserts/1516ipar.png",
                "ingredient": "Шоколадово брауни с парченца бял шоколад",
                "price": 3.9,
                "tag": {}
            },
            {
                "product_name": "Nirvana Pralines and Cream 150 ml",
                "product_picture": "deserts/1336ipar.png",
                "ingredient": "Сладолед с карамелов сироп и карамелизирани ядки",
                "price": 3.9,
                "tag": {}
            },
            {
                "product_name": "Nirvana Cookies and Cream 150 ml",
                "product_picture": "deserts/1335ipar.png",
                "ingredient": "Сладолед с аромат на ванилия и парченца какаови бисквитки",
                "price": 3.9,
                "tag": {}
            },
            {
                "product_name": "Nirvana Chocolate and Choco Chips 150 ml",
                "product_picture": "deserts/1549ipar.png",
                "ingredient": "Шоколадов сладолед с шоколадови парченца",
                "price": 3.9,
                "tag": {}
            }
        ]

        for data in deserts:
            item = Desert.objects.create(
                name=data['product_name'],
                description=data['ingredient'],
                image=data['product_picture'],
                price=data['price'],
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Desert: {item}'))
