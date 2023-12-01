# Generated by Django 4.2.7 on 2023-12-01 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cardquest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('rarity', models.CharField(choices=[('C', 'Common'), ('U', 'Uncommon'), ('R', 'Rare'), ('L', 'Legendary')], default='C', max_length=1)),
                ('hp', models.IntegerField(blank=True, null=True)),
                ('card_type', models.CharField(choices=[('fire', 'Fire'), ('water', 'Water'), ('grass', 'Grass'), ('electric', 'Electric'), ('psychic', 'Psychic'), ('fighting', 'Fighting'), ('dark', 'Dark'), ('steel', 'Steel'), ('fairy', 'Fairy'), ('dragon', 'Dragon'), ('normal', 'Normal'), ('ghost', 'Ghost'), ('ice', 'Ice'), ('bug', 'Bug'), ('rock', 'Rock'), ('ground', 'Ground'), ('poison', 'Poison'), ('flying', 'Flying'), ('none', 'None')], default='none', max_length=255)),
                ('attack', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('weakness', models.CharField(blank=True, max_length=255, null=True)),
                ('card_number', models.IntegerField(blank=True, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('evolution', models.BooleanField(default=False)),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cardquest.trainer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
