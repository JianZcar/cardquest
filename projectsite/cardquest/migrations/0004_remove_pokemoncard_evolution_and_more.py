# Generated by Django 4.2.7 on 2023-12-01 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardquest', '0003_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemoncard',
            name='evolution',
        ),
        migrations.RemoveField(
            model_name='pokemoncard',
            name='trainer',
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='abilities',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pokemoncard',
            name='evolution_stage',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]