# Generated by Django 2.2.24 on 2022-11-01 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20221101_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
