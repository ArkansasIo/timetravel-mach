"""Complete preliminary ETPS catalog for Systems 226–400."""
from pathlib import Path
import json

def load_systems(path=None):
    source = Path(path) if path else Path(__file__).resolve().parents[1] / "data" / "systems_226_400.json"
    payload = json.loads(source.read_text(encoding="utf-8"))
    systems = payload["systems"]
    ids = [item["id"] for item in systems]
    if len(ids) != 175 or ids != list(range(226, 401)):
        raise ValueError("catalog must contain each system ID from 226 through 400 exactly once")
    return systems

if __name__ == "__main__":
    systems = load_systems()
    print(f"Loaded {len(systems)} ETPS systems ({systems[0]['id']}–{systems[-1]['id']})")
