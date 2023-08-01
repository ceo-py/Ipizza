from django.core.management.base import BaseCommand

from apps.ingredients.models import Sauce


class Command(BaseCommand):
    help = 'Populate the Sauces model with initial data.'

    def handle(self, *args, **kwargs):
        Sauces = [
        "Моцарела",
        "Чедар сирене",
        "Веган Моцарела",
        "Краве сирене",
        "Топено сиренее",
        "Пармезан",
        "Ементалл"
      ]

        for item in Sauces:
            dough_type = Sauce.objects.create(
                name=item,
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Sauces: {dough_type}'))
