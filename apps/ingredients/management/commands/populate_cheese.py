from django.core.management.base import BaseCommand

from apps.ingredients.models import Cheese


class Command(BaseCommand):
    help = 'Populate the Cheese model with initial data.'

    def handle(self, *args, **kwargs):
        Cheeses = [
        "Моцарела",
        "Чедар сирене",
        "Веган Моцарела",
        "Краве сирене",
        "Топено сиренее",
        "Пармезан",
        "Ементалл"
      ]

        for item in Cheeses:
            create_object = Cheese.objects.create(
                name=item,
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Cheese: {create_object}'))
