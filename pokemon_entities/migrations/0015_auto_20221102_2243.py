# Generated by Django 2.2.24 on 2022-11-02 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0014_auto_20221102_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='pokemon_image',
            field=models.ImageField(blank=True, null=True, upload_to='./pokemons'),
        ),
    ]
