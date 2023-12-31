from django.core.management.base import BaseCommand
from ...models import PokemonCard, Trainer


class Command(BaseCommand):
    help = 'Creates initial data for the cardquest app'

    def handle(self, *args, **kwargs):
        self.create_pokemon_cards()
        self.create_trainers()

    @staticmethod
    def create_pokemon_cards():
        cards = [PokemonCard(
            name='Charizard',
            rarity='R',
            hp=120,
            card_type='fire',
            attack=250,
            description='Spits fire that is hot enough to melt boulders. Known to cause forest fires unintentionally.',
            weakness='water',
            card_number=1,
            release_date='1999-01-09',
            evolution_stage='stage 2',
            abilities='Blaze',
        ),
            PokemonCard(
                name='Blastoise',
                rarity='R',
                hp=120,
                card_type='water',
                attack=250,
                description='A brutal Pokémon with pressurized water jets on its shell. They are used for high speed tackles.',
                weakness='electric',
                card_number=2,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Torrent',
            ),
            PokemonCard(
                name='Venusaur',
                rarity='R',
                hp=120,
                card_type='grass',
                attack=250,
                description='The plant blooms when it is absorbing solar energy. It stays on the move to seek sunlight.',
                weakness='fire',
                card_number=3,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Overgrow',
            ),
            PokemonCard(
                name='Pikachu',
                rarity='R',
                hp=120,
                card_type='electric',
                attack=250,
                description='When several of these Pokémon gather, their electricity could build and cause lightning storms.',
                weakness='ground',
                card_number=4,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Static',
            ),
            PokemonCard(
                name='Mewtwo',
                rarity='R',
                hp=120,
                card_type='psychic',
                attack=250,
                description='It was created by a scientist after years of horrific gene splicing and DNA engineering experiments.',
                weakness='psychic',
                card_number=5,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Pressure',
            ),
            PokemonCard(
                name='Machamp',
                rarity='R',
                hp=120,
                card_type='fighting',
                attack=250,
                description='Using its heavy muscles, it throws powerful punches that can send the victim clear over the horizon.',
                weakness='psychic',
                card_number=6,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Guts',
            ),
            PokemonCard(
                name='Gengar',
                rarity='R',
                hp=120,
                card_type='dark',
                attack=250,
                description='Under a full moon, this Pokémon likes to mimic the shadows of people and laugh at their fright.',
                weakness='ghost',
                card_number=7,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Cursed Body',
            ),
            PokemonCard(
                name='Metagross',
                rarity='R',
                hp=120,
                card_type='steel',
                attack=250,
                description='Metagross has four brains in total. Combined, the four brains can breeze through difficult calculations faster than a supercomputer.',
                weakness='fire',
                card_number=8,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Clear Body',
            ),
            PokemonCard(
                name='Gardevoir',
                rarity='R',
                hp=120,
                card_type='fairy',
                attack=250,
                description='It has the ability to sense the feelings of others and it understands human speech.',
                weakness='steel',
                card_number=9,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Trace',
            ),
            PokemonCard(
                name='Rayquaza',
                rarity='R',
                hp=120,
                card_type='dragon',
                attack=250,
                description='It flies forever through the ozone layer, consuming meteoroids for sustenance.',
                weakness='ice',
                card_number=10,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Air Lock',
            ),
            PokemonCard(
                name='Snorlax',
                rarity='R',
                hp=120,
                card_type='normal',
                attack=250,
                description='It is not satisfied unless it eats over 880 pounds of food every day. When it is done eating, it goes promptly to sleep.',
                weakness='fighting',
                card_number=11,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Immunity',
            ),
            PokemonCard(
                name='Gengar',
                rarity='R',
                hp=120,
                card_type='ghost',
                attack=250,
                description='Under a full moon, this Pokémon likes to mimic the shadows of people and laugh at their fright.',
                weakness='ghost',
                card_number=12,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Cursed Body',
            ),
            PokemonCard(
                name='Articuno',
                rarity='R',
                hp=120,
                card_type='ice',
                attack=250,
                description='A legendary bird Pokémon. It can create blizzards by freezing moisture in the air.',
                weakness='fire',
                card_number=13,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Pressure',
            ),
            PokemonCard(
                name='Scyther',
                rarity='R',
                hp=120,
                card_type='bug',
                attack=250,
                description='With ninja-like agility and speed, it can create the illusion that there is more than one.',
                weakness='fire',
                card_number=14,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Swarm',
            ),
            PokemonCard(
                name='Golem',
                rarity='R',
                hp=120,
                card_type='rock',
                attack=250,
                description='Its boulder-like body is extremely hard. It can easily withstand dynamite blasts without damage.',
                weakness='water',
                card_number=15,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Sturdy',
            ),
            PokemonCard(
                name='Golem',
                rarity='R',
                hp=120,
                card_type='ground',
                attack=250,
                description='Its boulder-like body is extremely hard. It can easily withstand dynamite blasts without damage.',
                weakness='water',
                card_number=16,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Sturdy',
            ),
            PokemonCard(
                name='Golem',
                rarity='R',
                hp=120,
                card_type='rock',
                attack=250,
                description='Its boulder-like body is extremely hard. It can easily withstand dynamite blasts without damage.',
                weakness='water',
                card_number=17,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Sturdy',
            ),
            PokemonCard(
                name='Golem',
                rarity='R',
                hp=120,
                card_type='ground',
                attack=250,
                description='Its boulder-like body is extremely hard. It can easily withstand dynamite blasts without damage.',
                weakness='water',
                card_number=18,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Sturdy',
            ),
            PokemonCard(
                name='Golem',
                rarity='R',
                hp=120,
                card_type='rock',
                attack=250,
                description='Its boulder-like body is extremely hard. It can easily withstand dynamite blasts without damage.',
                weakness='water',
                card_number=19,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Sturdy',
            ),
            PokemonCard(
                name='Golem',
                rarity='R',
                hp=120,
                card_type='ground',
                attack=250,
                description='Its boulder-like body is extremely hard. It can easily withstand dynamite blasts without damage.',
                weakness='water',
                card_number=20,
                release_date='1999-01-09',
                evolution_stage='stage 2',
                abilities='Sturdy',
            ),]
        for card in cards:
            card.save()

    @staticmethod
    def create_trainers():
        trainers = [
            Trainer(
                name='Ash Ketchum',
                birthdate='1999-01-09',
                location='Pallet Town',
                email='ashketchum@email.com',),
            Trainer(
                name='Misty',
                birthdate='1999-01-09',
                location='Cerulean City',
                email='misty@email.com',),
            Trainer(
                name='Brock',
                birthdate='1999-01-09',
                location='Pewter City',
                email='brock@email.com',
            ),
            Trainer(
                name='Jessie',
                birthdate='1999-01-09',
                location='Team Rocket',
                email='jessi@email.com',
            ),
            Trainer(
                name='James',
                birthdate='1999-01-09',
                location='Team Rocket',
                email='ilovejesi@gmail.com',
            ),
            Trainer(
                name='Gary Oak',
                birthdate='1999-01-09',
                location='Pallet Town',
                email='goatlover@email.com',
            ),
            Trainer(
                name='Professor Oak',
                birthdate='1999-01-09',
                location='Pallet Town',
                email='profoak@email.com',
            ),
            Trainer(
                name='Professor Elm',
                birthdate='1999-01-09',
                location='New Bark Town',
                email='profelm@email.com',
            ),
            Trainer(
                name='Professor Birch',
                birthdate='1999-01-09',
                location='Littleroot Town',
                email='profbirch@email.com',
            ),
            Trainer(
                name='Professor Rowan',
                birthdate='1999-01-09',
                location='Sandgem Town',
                email='profrowan@email.com',
            ),
            ]

        for trainer in trainers:
            trainer.save()



