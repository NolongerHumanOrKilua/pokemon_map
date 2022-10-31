from pickle import TRUE
from django.db import models  # noqa F401

# your models here

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    pokemon_image = models.ImageField(null=True)

    def __str__(self):
        return format(self.title)
