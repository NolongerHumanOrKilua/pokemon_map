# Generated by Django 2.2.24 on 2022-11-10 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0032_auto_20221110_2228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='pokemons',
            new_name='pokemon',
        ),
    ]
