# Numerical experiments

## Experiment A — inertial time dilation
Question: how does proper time vary with constant speed for a fixed coordinate interval?
Model: τ=T√(1−β²), where T=10 s and β=v/c.
Independent variable: β from 0 to 0.99.
Output: CSV and PNG from `examples/plot_time_dilation.py`.
Expected limiting behavior: τ=T at rest and decreases monotonically as |β| approaches 1.
Classification: established special-relativistic formula under idealized assumptions; generated curve is synthetic calculation, not a measurement.

## Experiment B — gravitational clock ratio
Use `schwarzschild_static_clock_ratio(r, M)` for r>2GM/c². Sweep radius outside the Schwarzschild radius and plot dτ/dt. Clearly label the observer as static and the geometry as idealized Schwarzschild exterior.

## Experiment C — causal graph consistency
Create directed acyclic graphs for ordinary causal order. If introducing a cycle, report that it is a graph property and specify the additional consistency rule; a cycle is not evidence that physical time travel exists.

## Reporting template
- Question and hypothesis
- Equations and source
- Inputs, units, ranges, and constants
- Numerical method and precision
- Tests and limiting behavior
- Results and uncertainty
- Interpretation and limitations
