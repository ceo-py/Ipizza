import json
from django.core.management import BaseCommand
from django.core import serializers

from apps.pizza.models import Pizza


class Command(BaseCommand):
    help = 'Dump data to a JSON file with UTF-8 encoding'

    def add_arguments(self, parser):
        parser.add_argument('output_file', type=str)

    def handle(self, *args, **options):
        output_file = 'pizza.json'
        queryset = Pizza.objects.all()  # Replace YourModel with the model you want to dump
        data = serializers.serialize('json', queryset, ensure_ascii=False)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(data)