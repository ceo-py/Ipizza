from apps.dough_type.models import DoughType

# Adding dough types
dough_types_data = [
    {
        "type": "Средна",
        "picture": "https://www.dominos.bg/gallery/pansizes/bgiparTraditional_panbg.png",
        "description": "Нашето традиционно тесто",
        "price": 10.9
    },
    {
        "type": "Средна",
        "picture": "https://www.dominos.bg/gallery/pansizes/bgiparItalian_style_panbg.png",
        "description": "Тесто италиански стил",
        "price": 10.9
    },
    {
        "type": "Средна",
        "picture": "https://www.dominos.bg/gallery/pansizes/bgiparGluten_Freebg.png",
        "description": "Gluten Free Dough  (+ 3,10лв)",
        "price": 14.0
    },
    # Add more dough types in a similar manner
]

for dough_type_data in dough_types_data:
    DoughType.objects.create(**dough_type_data)