from django.core.management.base import BaseCommand

from apps.ingredients.models import Sauce


class Command(BaseCommand):
    help = 'Populate the Sauces model with initial data.'

    def handle(self, *args, **kwargs):
        Sauces = [
        "Сметана",
        "Барбекю сос",
        "Доматен сос"
      ]

        for item in Sauces:
            create_object = Sauce.objects.create(
                name=item,
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Sauces: {create_object}'))
