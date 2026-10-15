# Data dictionary

## Catalog CSV / JSON
- `id`: integer system identifier.
- `title`: short descriptive title.
- `status`: one of ESTABLISHED, ACTIVE_RESEARCH, TOY_MODEL, SPECULATIVE, FICTION.
- `summary`: scope note; not a substitute for the full model or evidence review.

## Simulation output
- `velocity_over_c`: dimensionless β=v/c, with |β|<1.
- `coordinate_seconds`: coordinate-time interval in seconds in the selected inertial frame.
- `proper_seconds`: proper time in seconds under the stated inertial flat-spacetime assumptions.

## Provenance requirements
Future datasets should add source URL/DOI, access date, measurement units, uncertainty, instrument or simulation method, software version, license, and data custodian. Never mix synthetic simulation rows with observational measurements without an explicit field separating them.
