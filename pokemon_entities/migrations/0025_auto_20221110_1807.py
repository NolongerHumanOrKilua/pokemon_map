# Generated by Django 2.2.24 on 2022-11-10 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0024_auto_20221110_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='evolution',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_evolution', to='pokemon_entities.Pokemon', verbose_name='Эволюция'),
        ),
    ]
