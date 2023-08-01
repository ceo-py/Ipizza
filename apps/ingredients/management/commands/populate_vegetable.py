from django.core.management.base import BaseCommand

from apps.ingredients.models import Vegetable


class Command(BaseCommand):
    help = 'Populate the Vegetable model with initial data.'

    def handle(self, *args, **kwargs):
        Vegetables = [
            "Моцарела",
            "Чедар сирене",
            "Веган Моцарела",
            "Краве сирене",
            "Топено сиренее",
            "Пармезан",
            "Ементалл"
        ]

        for item in Vegetables:
            dough_type = Vegetable.objects.create(
                name=item,
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Vegetable: {dough_type}'))
