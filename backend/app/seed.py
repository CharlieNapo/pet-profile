from datetime import date

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.pet import Pet, PetDocument

SEED_DATA = [
    {
        "name": "Bella",
        "date_of_birth": date(2022, 3, 10),
        "species": "dog",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-bella.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-bella.pdf"},
        ],
    },
    {
        "name": "Whiskers",
        "date_of_birth": date(2018, 11, 22),
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-whiskers.pdf"},
        ],
    },
    {
        "name": "Luna",
        "date_of_birth": date(2024, 6, 1),
        "species": "dog",
        "gender": "female",
        "documents": [],
    },
    {
        "name": "Max",
        "date_of_birth": date(2020, 8, 15),
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-max.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-max.pdf"},
            {"name": "Insurance Claim Form", "url": "https://docs.example.com/claim-max.pdf"},
        ],
    },
    {
        "name": "Cleo",
        "date_of_birth": date(2023, 4, 30),
        "species": "cat",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-cleo.pdf"},
        ],
    },
    {
        "name": "Charlie",
        "date_of_birth": date(2019, 1, 17),
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-charlie.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-charlie.pdf"},
        ],
    },
    {
        "name": "Milo",
        "date_of_birth": date(2021, 7, 3),
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-milo.pdf"},
        ],
    },
    {
        "name": "Daisy",
        "date_of_birth": date(2025, 2, 14),
        "species": "dog",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-daisy.pdf"},
        ],
    },
    {
        "name": "Oscar",
        "date_of_birth": date(2016, 9, 28),
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-oscar.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-oscar.pdf"},
        ],
    },
    {
        "name": "Poppy",
        "date_of_birth": date(2022, 12, 5),
        "species": "dog",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-poppy.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-poppy.pdf"},
        ],
    },
    {
        "name": "Simba",
        "date_of_birth": date(2017, 4, 11),
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-simba.pdf"},
        ],
    },
    {
        "name": "Rosie",
        "date_of_birth": date(2023, 8, 19),
        "species": "dog",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-rosie.pdf"},
        ],
    },
    {
        "name": "Teddy",
        "date_of_birth": date(2020, 2, 25),
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-teddy.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-teddy.pdf"},
            {"name": "Insurance Claim Form", "url": "https://docs.example.com/claim-teddy.pdf"},
        ],
    },
    {
        "name": "Nala",
        "date_of_birth": date(2024, 10, 8),
        "species": "cat",
        "gender": "female",
        "documents": [],
    },
    {
        "name": "Buddy",
        "date_of_birth": date(2015, 6, 30),
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-buddy.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-buddy.pdf"},
        ],
    },
    {
        "name": "Willow",
        "date_of_birth": date(2021, 3, 14),
        "species": "cat",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-willow.pdf"},
        ],
    },
    {
        "name": "Archie",
        "date_of_birth": date(2019, 12, 1),
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-archie.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-archie.pdf"},
        ],
    },
    {
        "name": "Lola",
        "date_of_birth": date(2022, 5, 22),
        "species": "cat",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-lola.pdf"},
        ],
    },
    {
        "name": "Rex",
        "date_of_birth": date(2013, 7, 9),
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-rex.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-rex.pdf"},
            {"name": "Insurance Claim Form", "url": "https://docs.example.com/claim-rex.pdf"},
        ],
    },
    {
        "name": "Misty",
        "date_of_birth": date(2018, 1, 3),
        "species": "cat",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-misty.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-misty.pdf"},
        ],
    },
    {
        "name": "Jasper",
        "date_of_birth": date(2024, 1, 27),
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-jasper.pdf"},
        ],
    },
    {
        "name": "Coco",
        "date_of_birth": date(2020, 11, 16),
        "species": "cat",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-coco.pdf"},
        ],
    },
    {
        "name": "Bailey",
        "date_of_birth": date(2016, 3, 8),
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-bailey.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-bailey.pdf"},
        ],
    },
    {
        "name": "Pepper",
        "date_of_birth": date(2023, 9, 12),
        "species": "cat",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-pepper.pdf"},
        ],
    },
    {
        "name": "Frankie",
        "date_of_birth": date(2021, 10, 5),
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-frankie.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-frankie.pdf"},
        ],
    },
    {
        "name": "Ginger",
        "date_of_birth": date(2017, 8, 20),
        "species": "cat",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-ginger.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-ginger.pdf"},
        ],
    },
    {
        "name": "Duke",
        "date_of_birth": date(2012, 4, 15),
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-duke.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-duke.pdf"},
            {"name": "Insurance Claim Form", "url": "https://docs.example.com/claim-duke.pdf"},
        ],
    },
    {
        "name": "Mittens",
        "date_of_birth": date(2025, 1, 9),
        "species": "cat",
        "gender": "female",
        "documents": [],
    },
    {
        "name": "Rocky",
        "date_of_birth": date(2019, 6, 24),
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-rocky.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-rocky.pdf"},
        ],
    },
    {
        "name": "Socks",
        "date_of_birth": date(2022, 8, 31),
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-socks.pdf"},
        ],
    },
    {
        "name": "Sadie",
        "date_of_birth": date(2014, 11, 18),
        "species": "dog",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-sadie.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-sadie.pdf"},
        ],
    },
    {
        "name": "Felix",
        "date_of_birth": date(2020, 4, 7),
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-felix.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-felix.pdf"},
        ],
    },
    {
        "name": "Molly",
        "date_of_birth": date(2023, 2, 28),
        "species": "dog",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-molly.pdf"},
        ],
    },
    {
        "name": "Tigger",
        "date_of_birth": date(2016, 12, 12),
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-tigger.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-tigger.pdf"},
        ],
    },
    {
        "name": "Cooper",
        "date_of_birth": date(2021, 1, 20),
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-cooper.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-cooper.pdf"},
        ],
    },
    {
        "name": "Pixie",
        "date_of_birth": date(2018, 5, 6),
        "species": "cat",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-pixie.pdf"},
        ],
    },
    {
        "name": "Bruno",
        "date_of_birth": date(2024, 3, 15),
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-bruno.pdf"},
        ],
    },
    {
        "name": "Shadow",
        "date_of_birth": date(2015, 10, 29),
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-shadow.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-shadow.pdf"},
        ],
    },
    {
        "name": "Ruby",
        "date_of_birth": date(2022, 7, 18),
        "species": "dog",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-ruby.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-ruby.pdf"},
        ],
    },
    {
        "name": "Smudge",
        "date_of_birth": date(2019, 9, 4),
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-smudge.pdf"},
        ],
    },
]


async def seed_pets(session: AsyncSession) -> None:
    result = await session.execute(select(func.count()).select_from(Pet))
    if result.scalar() != 0:
        return

    pets = []
    for data in SEED_DATA:
        docs_data = data.pop("documents", [])
        pet = Pet(**data)
        pet.documents = [PetDocument(**d) for d in docs_data]
        pets.append(pet)
        # Restore documents key so SEED_DATA stays intact if called again
        data["documents"] = docs_data

    session.add_all(pets)
    await session.commit()
