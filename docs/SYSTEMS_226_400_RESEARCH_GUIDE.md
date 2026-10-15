# Research guide for Systems 226–400

The machine-readable catalog contains 175 system records. To create an individual Markdown research file for every record, run:

```bash
python tools/generate_system_docs.py
```

The generator creates `docs/systems/226-...` through `docs/systems/400-...`. Each record includes a research question, assumptions, mathematical formulation, evidence/source requirements, reproducible-method section, results, limitations, and change log. Generated records are structured templates, not completed research papers. Fill them with sourced derivations and tested results before presenting them as finished research.

## Validation
```bash
python -m etps.catalog_complete
python -m unittest discover -s tests -v
```

The catalog test asserts every ID from 226 through 400 is present exactly once and that volume boundaries are correct.
