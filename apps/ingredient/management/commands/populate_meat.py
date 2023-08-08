from django.core.management.base import BaseCommand

from apps.ingredient.models import Meat


class Command(BaseCommand):
    help = "Populate the Meat model with initial data."

    def handle(self, *args, **kwargs):
        Meats = [
            "Пушен бекон",
            "Вентричина",
            "Пикантно телешко",
            "Риба тон",
            "Пушена шунка",
            "Чоризо",
            "Пеперони",
            "Пиле",
            "Пиле гирос",
        ]

        for item in Meats:
            create_object = Meat.objects.create(
                name=item,
            )
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created Meat: {create_object}")
            )
