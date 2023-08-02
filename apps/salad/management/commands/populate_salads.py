from django.core.management.base import BaseCommand
from apps.salad.models import Salad


class Command(BaseCommand):
    help = 'Populate the Salad model with initial data.'

    def handle(self, *args, **kwargs):
        salads = [
            {
                "product_name": "САЛАТА РОКА + СОС + ПРИБОРИ",
                "product_picture": "salads/1325large.png",
                "price": 7.3,
                "dough_types": [],
                "ingredients": [
                    "Пармезан",
                    "Пресни домати",
                    "Рукола"
                ],
                "ingredient_groups": {
                    "spices": [
                        "Риган",
                        "Песто сос",
                        "Крутон"
                    ],
                    "meats": [
                        "Пиле гирос",
                        "Пиле",
                        "Риба тон",
                        "Пушен бекон"
                    ],
                    "vegetables": [
                        "Пресни зелени чушки",
                        "Пресни домати",
                        "Царевица",
                        "Черни маслини",
                        "Лук",
                        "Сушени доматии",
                        "Рукола"
                    ],
                    "cheese": [
                        "Пармезан",
                        "Краве сирене"
                    ],
                    "sauce": []
                }
            },
            {
                "product_name": "САЛАТА ТРИКОЛОРЕ + ПРИБОРИ",
                "product_picture": "salads/1368large.png",
                "price": 7.3,
                "dough_types": [],
                "ingredients": [
                    "Песто сос",
                    "Краве сирене",
                    "Пресни домати"
                ],
                "ingredient_groups": {
                    "spices": [
                        "Риган",
                        "Песто сос",
                        "Крутон"
                    ],
                    "meats": [
                        "Пиле гирос",
                        "Пиле",
                        "Риба тон",
                        "Пушен бекон"
                    ],
                    "vegetables": [
                        "Пресни зелени чушки",
                        "Пресни домати",
                        "Царевица",
                        "Черни маслини",
                        "Лук",
                        "Сушени доматии",
                        "Рукола"
                    ],
                    "cheese": [
                        "Пармезан",
                        "Краве сирене"
                    ],
                    "sauce": []
                }
            },
            {
                "product_name": "САЛАТА ЦЕЗАР БЕКОН + СОС + ПРИБОРИ",
                "product_picture": "salads/1307large.png",
                "price": 8.9,
                "dough_types": [],
                "ingredients": [
                    "Крутон",
                    "Пармезан",
                    "Пушен бекон",
                    "Царевица"
                ],
                "ingredient_groups": {
                    "spices": [
                        "Риган",
                        "Песто сос",
                        "Крутон"
                    ],
                    "meats": [
                        "Пушен бекон",
                        "Пиле гирос",
                        "Пиле",
                        "Риба тон"
                    ],
                    "vegetables": [
                        "Сушени доматии",
                        "Рукола",
                        "Пресни зелени чушки",
                        "Пресни домати",
                        "Царевица",
                        "Черни маслини",
                        "Лук"
                    ],
                    "cheese": [
                        "Пармезан",
                        "Краве сирене"
                    ],
                    "sauce": []
                }
            },
            {
                "product_name": "САЛАТА ЦЕЗАР С ПИЛЕ +СОС + ПРИБОРИ",
                "product_picture": "salads/1308large.png",
                "price": 8.9,
                "dough_types": [],
                "ingredients": [
                    "Крутон",
                    "Пармезан",
                    "Пиле",
                    "Царевица"
                ],
                "ingredient_groups": {
                    "spices": [
                        "Риган",
                        "Песто сос",
                        "Крутон"
                    ],
                    "meats": [
                        "Пиле",
                        "Риба тон",
                        "Пушен бекон",
                        "Пиле гирос"
                    ],
                    "vegetables": [
                        "Пресни домати",
                        "Царевица",
                        "Черни маслини",
                        "Лук",
                        "Сушени доматии",
                        "Рукола",
                        "Пресни зелени чушки"
                    ],
                    "cheese": [
                        "Пармезан",
                        "Краве сирене"
                    ],
                    "sauce": []
                }
            },
            {
                "product_name": "САЛАТА РИБА ТОН + ПРИБОРИ",
                "product_picture": "salads/1328large.png",
                "price": 8.9,
                "dough_types": [],
                "ingredients": [
                    "Риба тон",
                    "Царевица",
                    "Черни маслини"
                ],
                "ingredient_groups": {
                    "spices": [
                        "Риган",
                        "Песто сос",
                        "Крутон"
                    ],
                    "meats": [
                        "Пиле гирос",
                        "Пиле",
                        "Риба тон",
                        "Пушен бекон"
                    ],
                    "vegetables": [
                        "Пресни зелени чушки",
                        "Пресни домати",
                        "Царевица",
                        "Черни маслини",
                        "Лук",
                        "Сушени доматии",
                        "Рукола"
                    ],
                    "cheese": [
                        "Пармезан",
                        "Краве сирене"
                    ],
                    "sauce": []
                }
            }
        ]

        for data in salads:
            item = Salad.objects.create(
                name=data['product_name'],
                description=', '.join(data['ingredients']),
                image=data['product_picture'],
                price=data['price'],
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Salad: {item}'))
