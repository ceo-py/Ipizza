from django.core.management.base import BaseCommand

from apps.dough_types.models import DoughType


class Command(BaseCommand):
    help = 'Populate the DoughType model with initial data.'

    def handle(self, *args, **kwargs):
        dough_types_data = [
            {
                "type": "Средна",
                "picture": "/dough/bgiparTraditional_panbg.png",
                "description": "Нашето традиционно тесто",
                "price": 10.9
            }
            ,

            {
                "type": "Средна",
                "picture": "/dough/bgiparItalian_style_panbg.png",
                "description": "Тесто италиански стил",
                "price": 10.9
            }
            ,

            {
                "type": "Средна",
                "picture": "/dough/bgiparGluten_Freebg.png",
                "description": "Gluten Free Dough  (+ 3,10лв)",
                "price": 14.0
            }
            ,

            {
                "type": "Голяма",
                "picture": "/dough/bgiparTraditional_panbg.png",
                "description": "Нашето традиционно тесто",
                "price": 14.0
            }
            ,

            {
                "type": "Голяма",
                "picture": "/dough/bgiparItalian_style_panbg.png",
                "description": "Тесто италиански стил",
                "price": 14.0
            }
            ,

            {
                "type": "Голяма",
                "picture": "/dough/bgiparThin_and_crispy_panbg.png",
                "description": "Тънко и хрупкаво тесто",
                "price": 14.0
            }
            ,

            {
                "type": "Голяма",
                "picture": "/dough/bgiparPhiladelphia_panbg.png",
                "description": "Прясно омесено тесто с коричка пълнена със сирене Philadelphia (+2,50лв)",
                "price": 16.5
            }
            ,

            {
                "type": "Голяма",
                "picture": "/dough/bgiparLarge_mozzarella_crustbg.png",
                "description": "Прясно омесено тесто с коричка, пълнена с моцарела (+2,50лв.)",
                "price": 16.5
            }
            ,

            {
                "type": "Голяма",
                "picture": "/dough/bgiparLarge_pepperoni_crustbg.png",
                "description": "Прясно омесено тесто с коричка, пълнена с пеперони (+2,50лв.)",
                "price": 16.5
            }
            ,

            {
                "type": "Джъмбо",
                "picture": "/dough/bgiparTraditional_panbg.png",
                "description": "Нашето традиционно тесто",
                "price": 15.4
            }
            ,

            {
                "type": "Джъмбо",
                "picture": "/dough/bgiparItalian_style_panbg.png",
                "description": "Тесто италиански стил",
                "price": 15.4
            }
        ]

        for data in dough_types_data:
            dough_type = DoughType.objects.create(
                type=data['type'],
                picture=data['picture'],
                description=data['description'],
                price=data['price']
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created DoughType: {dough_type}'))
