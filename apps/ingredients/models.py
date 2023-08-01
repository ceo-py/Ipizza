from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Spice(BaseModel):
    pass


class Meat(BaseModel):
    pass


class Vegetable(BaseModel):
    pass


class Cheese(BaseModel):
    pass


class Sauce(BaseModel):
    pass


class Tag(BaseModel):
    tag_image = models.ImageField(upload_to='tags/')