import httpx
from fastapi import APIRouter

from config.settings import settings

router = APIRouter()


@router.get("/health")
async def health() -> dict:
    return {"status": "ok"}


@router.get("/ready")
async def ready() -> dict:
    base = settings.vllm_base_url.rstrip("/")
    if base.endswith("/v1"):
        base = base[:-3]
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            r = await client.get(f"{base}/health")
            ok = r.status_code == 200
    except Exception:
        ok = False
    return {"ready": ok, "vllm": settings.vllm_base_url}