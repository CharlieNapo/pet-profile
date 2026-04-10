from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.pet import Pet, PetDocument

SEED_DATA = [
    {
        "name": "Bella",

        "species": "dog",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-bella.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-bella.pdf"},
        ],
    },
    {
        "name": "Whiskers",
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-whiskers.pdf"},
        ],
    },
    {
        "name": "Luna",
        "species": "dog",
        "gender": "female",
        "documents": [],
    },
    {
        "name": "Max",
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
        "species": "cat",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-cleo.pdf"},
        ],
    },
    {
        "name": "Charlie",
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-charlie.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-charlie.pdf"},
        ],
    },
    {
        "name": "Milo",
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-milo.pdf"},
        ],
    },
    {
        "name": "Daisy",
        "species": "dog",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-daisy.pdf"},
        ],
    },
    {
        "name": "Oscar",
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-oscar.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-oscar.pdf"},
        ],
    },
    {
        "name": "Poppy",
        "species": "dog",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-poppy.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-poppy.pdf"},
        ],
    },
    {
        "name": "Simba",
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-simba.pdf"},
        ],
    },
    {
        "name": "Rosie",
        "species": "dog",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-rosie.pdf"},
        ],
    },
    {
        "name": "Teddy",
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
        "species": "cat",
        "gender": "female",
        "documents": [],
    },
    {
        "name": "Buddy",
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-buddy.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-buddy.pdf"},
        ],
    },
    {
        "name": "Willow",
        "species": "cat",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-willow.pdf"},
        ],
    },
    {
        "name": "Archie",
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-archie.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-archie.pdf"},
        ],
    },
    {
        "name": "Lola",
        "species": "cat",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-lola.pdf"},
        ],
    },
    {
        "name": "Rex",
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
        "species": "cat",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-misty.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-misty.pdf"},
        ],
    },
    {
        "name": "Jasper",
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-jasper.pdf"},
        ],
    },
    {
        "name": "Coco",
        "species": "cat",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-coco.pdf"},
        ],
    },
    {
        "name": "Bailey",
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-bailey.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-bailey.pdf"},
        ],
    },
    {
        "name": "Pepper",
        "species": "cat",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-pepper.pdf"},
        ],
    },
    {
        "name": "Frankie",
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-frankie.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-frankie.pdf"},
        ],
    },
    {
        "name": "Ginger",
        "species": "cat",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-ginger.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-ginger.pdf"},
        ],
    },
    {
        "name": "Duke",
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
        "species": "cat",
        "gender": "female",
        "documents": [],
    },
    {
        "name": "Rocky",
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-rocky.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-rocky.pdf"},
        ],
    },
    {
        "name": "Socks",
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-socks.pdf"},
        ],
    },
    {
        "name": "Sadie",
        "species": "dog",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-sadie.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-sadie.pdf"},
        ],
    },
    {
        "name": "Felix",
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-felix.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-felix.pdf"},
        ],
    },
    {
        "name": "Molly",
        "species": "dog",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-molly.pdf"},
        ],
    },
    {
        "name": "Tigger",
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-tigger.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-tigger.pdf"},
        ],
    },
    {
        "name": "Cooper",
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-cooper.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-cooper.pdf"},
        ],
    },
    {
        "name": "Pixie",
        "species": "cat",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-pixie.pdf"},
        ],
    },
    {
        "name": "Bruno",
        "species": "dog",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-bruno.pdf"},
        ],
    },
    {
        "name": "Shadow",
        "species": "cat",
        "gender": "male",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-shadow.pdf"},
            {"name": "X-Ray Report", "url": "https://docs.example.com/xray-shadow.pdf"},
        ],
    },
    {
        "name": "Ruby",
        "species": "dog",
        "gender": "female",
        "documents": [
            {"name": "Vaccination Record", "url": "https://docs.example.com/vacc-ruby.pdf"},
            {"name": "Microchip Certificate", "url": "https://docs.example.com/chip-ruby.pdf"},
        ],
    },
    {
        "name": "Smudge",
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
