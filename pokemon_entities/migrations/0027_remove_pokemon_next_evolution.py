# Generated by Django 2.2.24 on 2022-11-10 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0026_auto_20221110_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='next_evolution',
        ),
    ]
