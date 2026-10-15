"""Complete preliminary ETPS catalog for Systems 226–400.
Generated data lives in data/systems_226_400.json and CSV.
"""
from pathlib import Path
import json

def load_systems(path=None):
    source = Path(path) if path else Path(__file__).resolve().parents[1] / "data" / "systems_226_400.json"
    payload = json.loads(source.read_text(encoding="utf-8"))
    systems = payload["systems"]
    ids = [item["id"] for item in systems]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate system IDs")
    if ids != list(range(226, 401)):
        raise ValueError("catalog must contain every ID from 226 through 400 in order")
    return systems

if __name__ == "__main__":
    entries = load_systems()
    print(f"Loaded {len(entries)} ETPS systems ({entries[0]['id']}–{entries[-1]['id']})")
