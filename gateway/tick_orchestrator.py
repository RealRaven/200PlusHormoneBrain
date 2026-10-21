import os
import time

from chemistry import loader, tick
from config.settings import settings

_USE_MEMORY = os.getenv("USE_MEMORY", "0") == "1"


class Orchestrator:
    def __init__(self) -> None:
        self.chemicals = loader.load_registry(settings.chemistry_dir)
        self.last_tick = time.time()
        # TODO(memory-branch): replace with real episodic/working stores
        self.episodic = None
        self.working = None

    def tick_state(self) -> dict[str, float]:
        now = time.time()
        tick.tick(self.chemicals, now - self.last_tick)
        self.last_tick = now
        return tick.snapshot(self.chemicals)

    def recall_for(self, message: str, state: dict[str, float]) -> list[str]:
        if not _USE_MEMORY:
            return []
        from memory.recall import recall  # local import — memory branch only
        return [m.content for m in recall(message, state, self.episodic.all(), limit=5)]

    def record(self, message: str, state: dict[str, float]) -> None:
        if not _USE_MEMORY:
            return
        from memory.base import MemoryEntry  # local import — memory branch only
        entry = MemoryEntry(content=message, state_snapshot=state)
        self.episodic.add(entry)
        self.working.add(entry)


_orchestrator: Orchestrator | None = None


def get_orchestrator() -> Orchestrator:
    global _orchestrator
    if _orchestrator is None:
        _orchestrator = Orchestrator()
    return _orchestrator