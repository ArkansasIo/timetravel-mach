# ETPS — Encyclopedia of Temporal Paradox Systems

A research-oriented, reproducible archive for temporal physics, relativistic spacetime, quantum information, causal structure, and explicitly labeled speculative models.

> **Scientific boundary:** this repository distinguishes established physics, active research, toy models, and fiction. It does not claim that time travel, traversable wormholes, causal inversion, or extra dimensions have been demonstrated.

## What's included
- Existing ETPS source text, preserved as `time` where present in the repository.
- Research volumes and system catalog for Systems 226–400.
- Python numerical models, plots, unit tests, JSON/CSV datasets, and SQL schema.
- Mathematical notes and Wolfram|Alpha query templates.
- Reproducible environment and CI configuration.

## Quick start
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m etps.cli list
python -m etps.cli simulate time-dilation --velocity 0.8
python -m unittest discover -s tests -v
```

Generated plots and CSV outputs are written to `artifacts/`.

## Evidence labels
- **ESTABLISHED** — well-tested theory or measurement within its domain.
- **ACTIVE_RESEARCH** — scientifically legitimate open question or incomplete theory.
- **TOY_MODEL** — simplified mathematical construction for exploration, not a prediction.
- **SPECULATIVE** — no empirical confirmation and/or substantial theoretical obstacles.
- **FICTION** — narrative concept rather than a physical claim.

See [docs/SCIENTIFIC_STATUS.md](docs/SCIENTIFIC_STATUS.md), [docs/ROADMAP.md](docs/ROADMAP.md), and [docs/MATHEMATICAL_AUDIT.md](docs/MATHEMATICAL_AUDIT.md).
