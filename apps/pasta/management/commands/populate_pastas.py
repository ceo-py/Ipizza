from django.core.management.base import BaseCommand

from apps.pasta.models import Pasta


class Command(BaseCommand):
    help = 'Populate the Pasta model with initial data.'

    def handle(self, *args, **kwargs):
        pastas = [
            {
                "product_name": "ПАСТА КАРБОНАРА + ПРИБОРИ",
                "product_picture": "pastas/front/1242large.png",
                "dough_types": [],
                "ingredients": [
                    "Сметана",
                    "Пармезан",
                    "Пушен бекон",
                    "Пресни гъби"
                ],
                "ingredient_groups": {
                    "spices": [
                        "Босилек",
                        "Песто сос",
                        "Риган",
                        "Пармезан снежинки"
                    ],
                    "meats": [
                        "Пушен бекон",
                        "Пиле",
                        "Пикантно телешко",
                        "Риба тон",
                        "Пеперони",
                        "Чоризо"
                    ],
                    "vegetables": [
                        "Сушени доматии",
                        "Лук",
                        "Царевица",
                        "Пресни гъби",
                        "Черни маслини",
                        "Пресни зелени чушки",
                        "Халапеньо-люти чушки",
                        "Пресни домати"
                    ],
                    "cheese": [
                        "Ементалл",
                        "Пармезан",
                        "Моцарела",
                        "Чедар сирене",
                        "Краве сирене"
                    ],
                    "sauce": [
                        "Барбекю сос",
                        "Доматен сос",
                        "Сметана"
                    ]
                },
                "product_main_picture": "/pastas/details/1242ipar.png",
                "product_main_description": "Паста, сметана, гъби, бекон, пармезан",
                "tag": {}
            },
            {
                "product_name": "НАПОЛИТАНА +ПРИБОРИ",
                "product_picture": "pastas/front/1243large.png",
                "dough_types": [],
                "ingredients": [
                    "Доматен сос",
                    "Песто сос",
                    "Пармезан"
                ],
                "ingredient_groups": {
                    "spices": [
                        "Босилек",
                        "Песто сос",
                        "Риган",
                        "Пармезан снежинки"
                    ],
                    "meats": [
                        "Пушен бекон",
                        "Пиле",
                        "Пикантно телешко",
                        "Риба тон",
                        "Пеперони",
                        "Чоризо"
                    ],
                    "vegetables": [
                        "Сушени доматии",
                        "Лук",
                        "Царевица",
                        "Пресни гъби",
                        "Черни маслини",
                        "Пресни зелени чушки",
                        "Халапеньо-люти чушки",
                        "Пресни домати"
                    ],
                    "cheese": [
                        "Чедар сирене",
                        "Краве сирене",
                        "Ементалл",
                        "Пармезан",
                        "Моцарела"
                    ],
                    "sauce": [
                        "Барбекю сос",
                        "Доматен сос",
                        "Сметана"
                    ]
                },
                "product_main_picture": "/pastas/details/1243ipar.png",
                "product_main_description": "Паста, доматен сос, песто, пармезан",
                "tag": {}
            },
            {
                "product_name": "ПАСТА ПЕПЕРОНИ +ПРИБОРИ",
                "product_picture": "pastas/front/843large.png",
                "dough_types": [],
                "ingredients": [
                    "Доматен сос",
                    "Сметана",
                    "Пармезан",
                    "Пеперони"
                ],
                "ingredient_groups": {
                    "spices": [
                        "Босилек",
                        "Песто сос",
                        "Риган",
                        "Пармезан снежинки"
                    ],
                    "meats": [
                        "Пушен бекон",
                        "Пиле",
                        "Пикантно телешко",
                        "Риба тон",
                        "Пеперони",
                        "Чоризо"
                    ],
                    "vegetables": [
                        "Сушени доматии",
                        "Лук",
                        "Царевица",
                        "Пресни гъби",
                        "Черни маслини",
                        "Пресни зелени чушки",
                        "Халапеньо-люти чушки",
                        "Пресни домати"
                    ],
                    "cheese": [
                        "Чедар сирене",
                        "Краве сирене",
                        "Ементалл",
                        "Пармезан",
                        "Моцарела"
                    ],
                    "sauce": [
                        "Барбекю сос",
                        "Доматен сос",
                        "Сметана"
                    ]
                },
                "product_main_picture": "/pastas/details/843ipar.png",
                "product_main_description": "Паста, доматен сос, сметана, пеперони, пармезан",
                "tag": {
                    "SPICY": "https://www.dominos.bg/images/tags/spicy.svg"
                }
            },
            {
                "product_name": "МАК ЕНД ЧИЙЗ +ПРИБОРИ",
                "product_picture": "pastas/front/1591large.png",
                "dough_types": [],
                "ingredients": [
                    "Сметана",
                    "Ементалл",
                    "Пармезан",
                    "Чедар сирене"
                ],
                "ingredient_groups": {
                    "spices": [
                        "Песто сос",
                        "Риган",
                        "Пармезан снежинки",
                        "Босилек"
                    ],
                    "meats": [
                        "Пикантно телешко",
                        "Риба тон",
                        "Пеперони",
                        "Чоризо",
                        "Пушен бекон",
                        "Пиле"
                    ],
                    "vegetables": [
                        "Царевица",
                        "Пресни гъби",
                        "Черни маслини",
                        "Пресни зелени чушки",
                        "Халапеньо-люти чушки",
                        "Пресни домати",
                        "Сушени доматии",
                        "Лук"
                    ],
                    "cheese": [
                        "Ементалл",
                        "Пармезан",
                        "Моцарела",
                        "Чедар сирене",
                        "Краве сирене"
                    ],
                    "sauce": [
                        "Барбекю сос",
                        "Доматен сос",
                        "Сметана"
                    ]
                },
                "product_main_picture": "/pastas/details/1591ipar.png",
                "product_main_description": "Паста, ементал, пармезан и чедър, сметана",
                "tag": {}
            }
        ]

        for data in pastas:
            item = Pasta.objects.create(
                name=data['product_name'],
                details_description=', '.join(data['ingredients']),
                details_image=data['product_picture'],
                front_image=data['product_main_picture'],
                front_description=data['product_main_description'],
                price=0,
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Pasta: {item}'))
