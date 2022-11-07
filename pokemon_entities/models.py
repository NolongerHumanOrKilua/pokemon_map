from django.db import models  # noqa F401

# your models here

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="название на русском")
    title_en = models.CharField(max_length=200, blank=True, verbose_name="название на английском")
    title_jp = models.CharField(max_length=200, blank=True, verbose_name="название на японском")
    pokemon_image = models.ImageField(null=True, blank=True, verbose_name="картинка покемона")
    description = models.TextField(blank=True, verbose_name="описание покемона")
    previous_evolution = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='+', verbose_name="из кого эволюционировал")
    next_evolution = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='+', verbose_name="в кого эволюционировал")

    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name="покемон")
    Lat = models.FloatField(blank=True, verbose_name="широта")
    Lon = models.FloatField(blank=True, verbose_name="долгота")
    appeared_at = models.DateTimeField(blank=True, null=True, verbose_name="был добавлен")
    disappeared_at = models.DateTimeField(blank=True, null=True, verbose_name="был убран")
    Level = models.IntegerField(blank=True, null=True, verbose_name="уровень")
    Health = models.IntegerField(blank=True, null=True, verbose_name="здоровье")
    Strenght = models.IntegerField(blank=True, null=True, verbose_name="сила")
    Defence = models.IntegerField(blank=True, null=True, verbose_name="защита")
    Stamina = models.IntegerField(blank=True, null=True, verbose_name="выносливость")