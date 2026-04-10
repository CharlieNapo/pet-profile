# Pet Profile

Internal tool for managing pet profiles used by the pet insurance platform.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and Docker Compose v2

## Quick Start

```bash
docker compose up --build
```

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000/api |
| API Docs (Swagger) | http://localhost:8000/docs |
| PostgreSQL | localhost:5432 |

The database is automatically migrated and seeded with 40 sample pets on first start.

## Architecture

```
pet-profile/
├── docker-compose.yml          # Orchestrates all services
├── backend/                    # Python 3.12 · FastAPI · SQLAlchemy · Alembic
│   ├── app/
│   │   ├── main.py             # FastAPI entry point
│   │   ├── models/pet.py       # ORM models (Pet, PetDocument)
│   │   ├── schemas/pet.py      # Pydantic response schemas
│   │   ├── routers/pets.py     # API route handlers
│   │   ├── services/           # Business logic layer
│   │   └── seed.py             # Seed data (40 pets)
│   ├── alembic/                # Database migrations
│   └── tests/                  # pytest test suite
└── frontend/                   # Node 24 · Next.js 16 · React 19 · TypeScript
    └── src/
        ├── app/                # Pages (App Router)
        ├── components/         # React components
        └── lib/api.ts          # Backend API client
```

## Useful Commands

```bash
# Start all services
docker compose up --build

# Stop all services
docker compose down

# Stop and reset database
docker compose down -v

# View backend logs
docker compose logs -f backend

# Run backend tests
docker compose exec backend uv run pytest

# Create a new migration
docker compose exec backend uv run alembic revision --autogenerate -m "description"

# Apply migrations manually
docker compose exec backend uv run alembic upgrade head
```
