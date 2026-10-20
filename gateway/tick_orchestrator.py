import time

from chemistry import loader, tick
from config.settings import settings
from memory.base import MemoryEntry
from memory.episodic import EpisodicMemory
from memory.recall import recall
from memory.working import WorkingMemory


class Orchestrator:
    def __init__(self) -> None:
        self.chemicals = loader.load_registry(settings.chemistry_dir)
        self.episodic = EpisodicMemory(settings.memory_file)
        self.working = WorkingMemory()
        self.last_tick = time.time()

    def tick_state(self) -> dict[str, float]:
        now = time.time()
        tick.tick(self.chemicals, now - self.last_tick)
        self.last_tick = now
        return tick.snapshot(self.chemicals)

    def recall_for(self, message: str, state: dict[str, float]) -> list[str]:
        matches = recall(message, state, self.episodic.all(), limit=5)
        return [m.content for m in matches]

    def record(self, message: str, state: dict[str, float]) -> None:
        entry = MemoryEntry(content=message, state_snapshot=state)
        self.episodic.add(entry)
        self.working.add(entry)


_orchestrator: Orchestrator | None = None


def get_orchestrator() -> Orchestrator:
    global _orchestrator
    if _orchestrator is None:
        _orchestrator = Orchestrator()
    return _orchestrator