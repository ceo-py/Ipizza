from django.core.management.base import BaseCommand

from apps.ingredient.models import Spice


class Command(BaseCommand):
    help = 'Populate the Spice model with initial data.'

    def handle(self, *args, **kwargs):
        Spices = [
            "Босилек",
            "Песто сос",
            "Пармезан снежинки",
            "Риган"
        ]

        for item in Spices:
            create_object = Spice.objects.create(
                name=item,
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Spice: {create_object}'))
