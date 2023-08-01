from django.core.management.base import BaseCommand

from apps.ingredients.models import Vegetable


class Command(BaseCommand):
    help = 'Populate the Vegetable model with initial data.'

    def handle(self, *args, **kwargs):
        Vegetables = [
            "Сушени доматии",
            "Лук",
            "Халапеньо-люти чушки",
            "Пресни гъби",
            "Карамелизиран лук",
            "Ананас",
            "Пресни зелени чушки",
            "Кисeли краставички",
            "Пресни домати",
            "Царевица",
            "Рукола",
            "Черни маслини"
        ]

        for item in Vegetables:
            create_object = Vegetable.objects.create(
                name=item,
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Vegetable: {create_object}'))
