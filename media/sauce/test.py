dough_types =   [
  {
    "product_name": "Медена Горчица",
    "product_picture": "https://www.dominos.bg/gallery/fmobile/1366ipar.png",
    "ingredient": "",
    "price": 1.0,
    "tag": {}
  },
  {
    "product_name": "Чеснов coc",
    "product_picture": "https://www.dominos.bg/gallery/fmobile/1201ipar.png",
    "ingredient": "",
    "price": 1.0,
    "tag": {}
  },
  {
    "product_name": "Барбекю сос",
    "product_picture": "https://www.dominos.bg/gallery/fmobile/1200ipar.png",
    "ingredient": "",
    "price": 1.0,
    "tag": {}
  },
  {
    "product_name": "Чили сос",
    "product_picture": "https://www.dominos.bg/gallery/fmobile/1202ipar.png",
    "ingredient": "",
    "price": 1.0,
    "tag": {}
  },
  {
    "product_name": "Доматен сос",
    "product_picture": "https://www.dominos.bg/gallery/fmobile/1206ipar.png",
    "ingredient": "",
    "price": 1.0,
    "tag": {}
  },
  {
    "product_name": "Млечен сос",
    "product_picture": "https://www.dominos.bg/gallery/fmobile/1207ipar.png",
    "ingredient": "",
    "price": 1.0,
    "tag": {}
  },
  {
    "product_name": "Ранч сос",
    "product_picture": "https://www.dominos.bg/gallery/fmobile/1205ipar.png",
    "ingredient": "",
    "price": 1.0,
    "tag": {}
  },
  {
    "product_name": "Цезар сос",
    "product_picture": "https://www.dominos.bg/gallery/fmobile/1512ipar.png",
    "ingredient": "Цезар сос",
    "price": 1.0,
    "tag": {}
  },
  {
    "product_name": "Балсамов дресинг",
    "product_picture": "https://www.dominos.bg/gallery/fmobile/1646ipar.png",
    "ingredient": "Балсамов дресинг",
    "price": 1.0,
    "tag": {}
  }
]
import requests

for x in dough_types:
    # print(x['product_picture'])
    # print(x['product_main_picture'])
    image_name = x['product_picture'].split('/')[-1]


    imageURL = x['product_picture']
    # imageURL = f"https://{x['product_picture']}"
    response = requests.get(imageURL)

    with open(image_name, "wb") as imageFile:
        imageFile.write(response.content)
        print(f'{image_name} download completed.')