import json

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from config.settings import settings
from gateway.prompt_builder import build_messages
from gateway.schemas import ChatRequest
from gateway.tick_orchestrator import get_orchestrator
from gateway.vllm_client import get_client

router = APIRouter()


def _sse(event: dict) -> str:
    return f"data: {json.dumps(event)}\n\n"


async def _stream_chat(message: str):
    orch = get_orchestrator()
    state = orch.tick_state()
    yield _sse({"type": "state", "data": state})

    recalled = orch.recall_for(message, state)
    messages = build_messages(state, recalled, message)

    client = get_client()
    internal_acc: list[str] = []
    spoken_acc: list[str] = []
    buffer = ""
    mode: str | None = None

    try:
        stream = await client.chat.completions.create(
            model=settings.model_id,
            messages=messages,
            max_tokens=settings.max_tokens,
            temperature=settings.temperature,
            stream=True,
        )
        async for chunk in stream:
            delta = chunk.choices[0].delta.content or ""
            buffer += delta

            while True:
                if mode is None:
                    if "<internal>" in buffer:
                        buffer = buffer.split("<internal>", 1)[1]
                        mode = "internal"
                    elif "<spoken>" in buffer:
                        buffer = buffer.split("<spoken>", 1)[1]
                        mode = "spoken"
                    else:
                        if len(buffer) > 20:
                            buffer = buffer[-20:]
                        break
                elif mode == "internal":
                    if "</internal>" in buffer:
                        content, buffer = buffer.split("</internal>", 1)
                        if content:
                            internal_acc.append(content)
                            yield _sse({"type": "internal_delta", "content": content})
                        mode = None
                    else:
                        if buffer:
                            internal_acc.append(buffer)
                            yield _sse({"type": "internal_delta", "content": buffer})
                            buffer = ""
                        break
                elif mode == "spoken":
                    if "</spoken>" in buffer:
                        content, buffer = buffer.split("</spoken>", 1)
                        if content:
                            spoken_acc.append(content)
                            yield _sse({"type": "spoken_delta", "content": content})
                        mode = None
                    else:
                        if buffer:
                            spoken_acc.append(buffer)
                            yield _sse({"type": "spoken_delta", "content": buffer})
                            buffer = ""
                        break
    except Exception as exc:
        yield _sse({"type": "error", "message": str(exc)})

    orch.record(message, state)
    yield _sse(
        {
            "type": "done",
            "internal": "".join(internal_acc),
            "spoken": "".join(spoken_acc),
        }
    )


@router.post("/chat")
async def chat(req: ChatRequest):
    return StreamingResponse(
        _stream_chat(req.message),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )