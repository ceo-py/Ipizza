from django.core.management.base import BaseCommand

from apps.ingredients.models import Tag


class Command(BaseCommand):
    help = 'Populate the Tag model with initial data.'

    def handle(self, *args, **kwargs):
        Tags = {
            "VEGETARIAN": "/tags/vegetarian.svg",
            "PREMIUM": "/tags/premium.svg",
            "НОВО": "/tags/new_product.svg",
            "SPICY": "/tags/spicy.svg"
        }

        for k, v in Tags.items():
            create_object = Tag.objects.create(
                name=k,
                tag_image=v
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created Tag: {create_object}'))
