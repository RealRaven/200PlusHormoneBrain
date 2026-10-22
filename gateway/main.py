from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from gateway.routes import chat, health, state


@asynccontextmanager
async def lifespan(app: FastAPI):
    from gateway.tick_orchestrator import get_orchestrator

    get_orchestrator()  # warm up chemistry + memory
    yield


app = FastAPI(title="200PlusHormoneBrain Gateway", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(health.router, tags=["health"])
app.include_router(chat.router, tags=["chat"])
app.include_router(state.router, tags=["state"])


if __name__ == "__main__":
    import uvicorn

    from config.settings import settings

    uvicorn.run(
        "gateway.main:app",
        host=settings.gateway_host,
        port=settings.gateway_port,
    )