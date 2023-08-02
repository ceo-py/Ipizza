from django.core.management.base import BaseCommand

from apps.sandwich.models import Sandwich


class Command(BaseCommand):
    help = 'Populate the Sandwich model with initial data.'

    def handle(self, *args, **kwargs):
        sandwichs = [
            {
                "product_name": "САНДВИЧ ПЕПЕРОНИ",
                "product_picture": "sandwich/1472large.png",
                "price": 7.9,
                "dough_types": [],
                "ingredients": [
                    "Доматен сос",
                    "Пеперони"
                ],
                "ingredient_groups": {
                    "spices": [],
                    "meats": [
                        "Пиле гирос",
                        "Пушен бекон",
                        "Вентричина",
                        "Пиле",
                        "Пушена шунка",
                        "Пеперони"
                    ],
                    "vegetables": [
                        "Сушени доматии",
                        "Лук",
                        "Рукола",
                        "Кисeли краставички",
                        "Пресни зелени чушки",
                        "Царевица",
                        "Пресни домати",
                        "Черни маслини"
                    ],
                    "cheese": [
                        "Чедар сирене",
                        "Ементалл",
                        "Моцарела",
                        "Краве сирене"
                    ],
                    "sauce": [
                        "Доматен сос",
                        "Барбекю сос"
                    ]
                }
            },
            {
                "product_name": "САНДВИЧ БАРБЕКЮ ПИЛЕ",
                "product_picture": "sandwich/1471large.png",
                "price": 7.9,
                "dough_types": [],
                "ingredients": [
                    "Барбекю сос",
                    "Пушен бекон",
                    "Пиле"
                ],
                "ingredient_groups": {
                    "spices": [],
                    "meats": [
                        "Пиле гирос",
                        "Пушен бекон",
                        "Вентричина",
                        "Пиле",
                        "Пушена шунка",
                        "Пеперони"
                    ],
                    "vegetables": [
                        "Сушени доматии",
                        "Лук",
                        "Рукола",
                        "Кисeли краставички",
                        "Пресни зелени чушки",
                        "Царевица",
                        "Пресни домати",
                        "Черни маслини"
                    ],
                    "cheese": [
                        "Чедар сирене",
                        "Ементалл",
                        "Моцарела",
                        "Краве сирене"
                    ],
                    "sauce": [
                        "Доматен сос",
                        "Барбекю сос"
                    ]
                }
            },
            {
                "product_name": "САНДВИЧ МЕДИТЕРАНЕО",
                "product_picture": "sandwich/1470large.png",
                "price": 7.9,
                "dough_types": [],
                "ingredients": [
                    "Краве сирене",
                    "Пресни зелени чушки",
                    "Пресни домати",
                    "Черни маслини"
                ],
                "ingredient_groups": {
                    "spices": [],
                    "meats": [
                        "Пиле гирос",
                        "Пушен бекон",
                        "Вентричина",
                        "Пиле",
                        "Пушена шунка",
                        "Пеперони"
                    ],
                    "vegetables": [
                        "Сушени доматии",
                        "Лук",
                        "Рукола",
                        "Кисeли краставички",
                        "Пресни зелени чушки",
                        "Царевица",
                        "Пресни домати",
                        "Черни маслини"
                    ],
                    "cheese": [
                        "Чедар сирене",
                        "Ементалл",
                        "Моцарела",
                        "Краве сирене"
                    ],
                    "sauce": [
                        "Доматен сос",
                        "Барбекю сос"
                    ]
                }
            },
            {
                "product_name": "Сандвич Пастрами",
                "product_picture": "https://sandwich/1663ipar.png",
                "price": 11.9,
                "ingredients":[]
            }
        ]

        for data in sandwichs:
            item = Sandwich.objects.create(
                name=data['product_name'],
                description=', '.join(data['ingredients']),
                image=data['product_picture'],
                price=data['price'],
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Sandwich: {item}'))
