from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import text

from app.database import async_session_factory
from app.routers.pets import router as pets_router
from app.seed import seed_pets


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with async_session_factory() as session:
        await seed_pets(session)
    yield


app = FastAPI(title="Pet Profile API", lifespan=lifespan)

# Permissive CORS — appropriate for this internal interview tool.
# Restrict origins in a real production deployment.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pets_router)


@app.get("/health")
async def health():
    try:
        async with async_session_factory() as session:
            await session.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception:
        return JSONResponse({"status": "unhealthy"}, status_code=503)
