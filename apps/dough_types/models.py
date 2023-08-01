from django.db import models


class DoughType(models.Model):
    DOUGH_SIZES = (
        ('Средна', 'Средна'),
        ('Голяма', 'Голяма'),
        ('Джъмбо', 'Джъмбо'),
    )

    type = models.CharField(max_length=100, choices=DOUGH_SIZES)
    picture = models.URLField()
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return f'{self.type} - {self.description}'
