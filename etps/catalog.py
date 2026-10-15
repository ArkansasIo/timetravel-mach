"""Machine-readable catalog for ETPS systems 226–400."""
SYSTEMS = [
 {"id": 226, "title": "Quantum Causal Networks", "status": "ACTIVE_RESEARCH", "summary": "Graph models of causal order and quantum processes."},
 {"id": 227, "title": "Temporal Superposition (Toy Model)", "status": "TOY_MODEL", "summary": "A formal analogy, not a demonstrated ability to superpose macroscopic histories."},
 {"id": 228, "title": "Measurement and Temporal Records", "status": "ACTIVE_RESEARCH", "summary": "Measurement records, decoherence, and time-dependent observables."},
 {"id": 229, "title": "Quantum Entanglement Across Time", "status": "ACTIVE_RESEARCH", "summary": "Temporal correlations and postselected experiments; not backward messaging."},
 {"id": 230, "title": "Density Matrices and Purity", "status": "ESTABLISHED", "summary": "Density operators, trace, purity, and von Neumann entropy."},
 {"id": 231, "title": "Temporal Quantum Channels", "status": "ACTIVE_RESEARCH", "summary": "Quantum channels and process descriptions with time labels."},
 {"id": 232, "title": "Paradox Loop Constraint (Toy Model)", "status": "TOY_MODEL", "summary": "Fixed-point consistency as a mathematical assumption."},
 {"id": 233, "title": "Temporal Quantum Field Notes", "status": "ACTIVE_RESEARCH", "summary": "Quantum fields in spacetime; no validated temporal-control technology implied."},
 {"id": 234, "title": "Temporal Qubit Analogy", "status": "TOY_MODEL", "summary": "A pedagogical state encoding with explicit ordinary-time semantics."},
 {"id": 235, "title": "Quantum Multiverse Processor", "status": "FICTION", "summary": "Narrative computing concept, not a known computational architecture."},
 {"id": 301, "title": "Special-Relativistic Time Dilation", "status": "ESTABLISHED", "summary": "Proper time along timelike worldlines."},
 {"id": 302, "title": "Gravitational Clock Rates", "status": "ESTABLISHED", "summary": "Weak-field and Schwarzschild exterior clock-rate comparisons."},
 {"id": 303, "title": "Wormhole Time-Shift Proposal", "status": "SPECULATIVE", "summary": "Mathematical discussion contingent on unverified traversable wormholes and exotic conditions."},
 {"id": 304, "title": "Closed Timelike Curves", "status": "ACTIVE_RESEARCH", "summary": "Solutions and causal pathologies in selected spacetime geometries."},
 {"id": 305, "title": "Black-Hole Horizons and Proper Time", "status": "ESTABLISHED", "summary": "Relativistic geometry; distinguish coordinate effects from local measurements."},
 {"id": 306, "title": "Extra Dimensions", "status": "SPECULATIVE", "summary": "Hypothetical dimensions in some high-energy frameworks, not observed directly."},
 {"id": 307, "title": "Cosmological Expansion", "status": "ESTABLISHED", "summary": "Scale factor and expansion history in cosmology."},
 {"id": 308, "title": "Entropy and the Arrow of Time", "status": "ACTIVE_RESEARCH", "summary": "Statistical-mechanical account of macroscopic temporal asymmetry."},
 {"id": 309, "title": "Causal Graphs", "status": "ACTIVE_RESEARCH", "summary": "Directed graphs as models of causal structure; interpretation depends on model."},
 {"id": 310, "title": "Energy-Time Relations", "status": "ESTABLISHED", "summary": "Context-dependent quantum energy-time relations; not identical to position-momentum uncertainty."},
]
def list_systems():
    return sorted(SYSTEMS, key=lambda item: item["id"])
