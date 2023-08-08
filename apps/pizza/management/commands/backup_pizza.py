from django.apps import apps
from django.core import serializers
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Dump data to a JSON file with UTF-8 encoding"

    def add_arguments(self, parser):
        parser.add_argument("output_file", type=str)

    def get_all_model_instances(self):
        all_models = apps.get_models()
        all_instances = []

        for model in all_models:
            str_model = str(model)
            if "User" in str_model or "apps" not in str_model:
                continue
            print(model)
            model_instances = model.objects.all()
            all_instances.extend(model_instances)

        return all_instances

    def handle(self, *args, **options):
        output_file = options["output_file"]
        all_instances = self.get_all_model_instances()
        data = serializers.serialize("json", all_instances, ensure_ascii=False)

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(data)


"""
save backup db => python manage.py dumpdata_utf8 output_fileB.json
load backup db => python .\manage.py loaddata .\output_fileB.json
"""
