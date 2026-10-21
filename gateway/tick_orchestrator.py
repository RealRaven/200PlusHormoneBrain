import os
import threading
import time

from gateway import tick, loader, settings

_USE_MEMORY = os.getenv("USE_MEMORY", "0") == "1"

if _USE_MEMORY:
    raise RuntimeError(
        "USE_MEMORY=1 is not supported on this branch: the 'memory' package "
        "(memory.recall, memory.base) has not been implemented yet. "
        "Unset USE_MEMORY or set it to '0'."
    )


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
        # Memory is not implemented on this branch (see module-level guard).
        return []

    def record(self, message: str, state: dict[str, float]) -> None:
        # Memory is not implemented on this branch (see module-level guard).
        return


_orchestrator: Orchestrator | None = None
_orchestrator_lock = threading.Lock()


def get_orchestrator() -> Orchestrator:
    global _orchestrator
    if _orchestrator is None:
        with _orchestrator_lock:
            if _orchestrator is None:
                _orchestrator = Orchestrator()
    return _orchestrator