"""Generate one Markdown research record per ETPS system in the complete catalog."""
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "systems_226_400.json"
DEST = ROOT / "docs" / "systems"

def slugify(value):
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-").replace("--", "-")

def render(system):
    title = system["title"]
    return f"""# System {system['id']}: {title}

- **Volume:** {system['volume']}
- **Preliminary status:** {system['status']}
- **Catalog summary:** {system['summary']}

## Research question
What precise, falsifiable question can be answered about {title.lower()} under an explicitly defined mathematical and physical model?

## Definitions and assumptions
Record every variable, its SI unit, sign convention, coordinate system, initial condition, boundary condition, and domain of validity. Separate assumptions from consequences derived from them.

## Mathematical formulation
Add the governing equations here with LaTeX notation. Define every symbol directly below each equation. Perform dimensional analysis and test limiting cases. Do not invent a universal equation when the model is context-dependent.

## Evidence and prior work
Add verified textbook, peer-reviewed, official-data, or primary-source references. Record DOI or stable URL and access date where applicable. Do not fabricate citations. Distinguish established evidence from interpretation and speculation.

## Reproducible method
Describe analytical derivation, numerical method, input data, software version, tolerances, tests, and expected outputs. Label generated data as simulated and measured data as observational.

## Results
Populate only after a derivation, calculation, or experiment has been performed. Include uncertainty, sensitivity analysis, counterexamples, and failed runs where relevant.

## Limitations and falsifiability
State what the model cannot establish and identify observations or results that would count against the hypothesis. Mathematical consistency alone does not establish physical realizability.

## Change log
- Initial generated record from the ETPS catalog. Requires expert review and source-backed completion.
"""

def main():
    payload = json.loads(SOURCE.read_text(encoding="utf-8"))
    systems = payload["systems"]
    if len(systems) != 175 or [s["id"] for s in systems] != list(range(226, 401)):
        raise ValueError("Expected exactly Systems 226–400, without gaps or duplicate IDs")
    DEST.mkdir(parents=True, exist_ok=True)
    for system in systems:
        (DEST / f"{system['id']}-{slugify(system['title'])}.md").write_text(render(system), encoding="utf-8")
    print(f"Generated {len(systems)} research records in {DEST.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
