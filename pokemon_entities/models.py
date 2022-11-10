from django.db import models  # noqa F401

# your models here

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="название на русском")
    title_en = models.CharField(max_length=200, blank=True, verbose_name="название на английском")
    title_jp = models.CharField(max_length=200, blank=True, verbose_name="название на японском")
    pokemon_image = models.ImageField(null=True, blank=True, verbose_name="картинка покемона")
    description = models.TextField(blank=True, verbose_name="описание покемона")
    previous_evolution = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='next_evolution', verbose_name="Эволюция")

    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entities', verbose_name="покемон")
    lat = models.FloatField(blank=True, verbose_name="широта")
    lon = models.FloatField(blank=True, verbose_name="долгота")
    appeared_at = models.DateTimeField(blank=True, null=True, verbose_name="был добавлен")
    disappeared_at = models.DateTimeField(blank=True, null=True, verbose_name="был убран")
    level = models.IntegerField(blank=True, null=True, verbose_name="уровень")
    health = models.IntegerField(blank=True, null=True, verbose_name="здоровье")
    strenght = models.IntegerField(blank=True, null=True, verbose_name="сила")
    defence = models.IntegerField(blank=True, null=True, verbose_name="защита")
    stamina = models.IntegerField(blank=True, null=True, verbose_name="выносливость")