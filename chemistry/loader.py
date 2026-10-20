from pathlib import Path

import yaml

from chemistry.tick import Chemical


def load_registry(root: str | Path = "infrastructure/chemicals_hormones") -> dict[str, Chemical]:
    root = Path(root)
    if not root.is_dir():
        raise FileNotFoundError(f"Chemistry directory not found: {root}")

    chemicals: dict[str, Chemical] = {}

    # Each category subfolder (01_..., 02_..., etc.) contains one hormones.yaml
    for category_dir in sorted(root.iterdir()):
        if not category_dir.is_dir():
            continue
        yaml_path = category_dir / "hormones.yaml"
        if not yaml_path.is_file():
            continue
        with open(yaml_path) as f:
            entries = yaml.safe_load(f) or []
        for entry in entries:
            chem_id = entry["id"]
            chemicals[chem_id] = Chemical(
                id=chem_id,
                name=entry.get("name", chem_id),
                baseline_level=float(entry.get("baseline_level", 0.5)),
                half_life_minutes=float(entry.get("half_life_minutes", 60)),
                type=entry.get("type", ""),
                molecular_formula=entry.get("molecular_formula", ""),
                units=entry.get("units", ""),
                reference_range=entry.get("reference_range", []),
                precursors=entry.get("precursors", []),
                released_by=entry.get("released_by", []),
                tags=entry.get("tags", []),
                aliases=entry.get("aliases", []),
            )
    return chemicals