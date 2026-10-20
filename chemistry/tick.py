from dataclasses import dataclass, field


@dataclass
class Chemical:
    id: str
    name: str
    baseline_level: float = 0.5          # 0–1, matches your YAML
    half_life_minutes: float = 60.0
    current: float = 0.0
    type: str = ""
    molecular_formula: str = ""
    units: str = ""
    reference_range: list[float] = field(default_factory=list)
    precursors: list[str] = field(default_factory=list)
    released_by: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    aliases: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.current == 0.0:
            self.current = self.baseline_level


def tick(chemicals: dict[str, Chemical], dt_seconds: float) -> None:
    """Exponential decay toward baseline_level (0–1 scale)."""
    if dt_seconds <= 0:
        return
    for chem in chemicals.values():
        half_life_seconds = max(chem.half_life_minutes * 60.0, 0.1)
        decay = 0.5 ** (dt_seconds / half_life_seconds)
        chem.current = chem.baseline_level + (chem.current - chem.baseline_level) * decay


def snapshot(chemicals: dict[str, Chemical]) -> dict[str, float]:
    """Emit 0–100 for the prompt / UI, preserving the 0–1 YAML scale internally."""
    return {chem.name: round(chem.current * 100.0, 2) for chem in chemicals.values()}