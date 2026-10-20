from fastapi import APIRouter

from gateway.tick_orchestrator import get_orchestrator

router = APIRouter()


@router.get("/state")
async def get_state() -> dict:
    orch = get_orchestrator()
    return {"state": orch.tick_state()}