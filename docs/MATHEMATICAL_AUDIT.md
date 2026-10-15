# Mathematical audit — initial checklist

This audit provides a safer mathematical baseline for extending the existing ETPS manuscript.

## Relativistic time dilation
For inertial relative speed v in flat spacetime:
`gamma = 1 / sqrt(1 - v²/c²)`; `Δτ = Δt/gamma`.
Conditions: |v| < c; constant relative speed; inertial frame setup. This is not a model of arbitrary acceleration or curved spacetime.

## Schwarzschild static clock
For a static observer outside a non-rotating spherical mass:
`dτ/dt = sqrt(1 - 2GM/(rc²))`.
Conditions: exterior Schwarzschild geometry, r > 2GM/c², static observer. It does not apply unchanged to rotating black holes or arbitrary trajectories.

## Mass-energy
`E₀ = mc²` is rest energy. It is not a complete formula for the total energy of a moving object; relativistic total energy is `E² = (pc)² + (mc²)²`.

## Quantum density matrices
A density operator obeys `ρ = ρ†`, `Tr(ρ)=1`, and is positive semidefinite. Purity is `Tr(ρ²)`; von Neumann entropy is `S(ρ)=-Tr(ρ ln ρ)` (units depend on logarithm convention).

## Energy-time relations
Do not present ΔEΔt ≥ ℏ/2 as a context-free universal theorem. Energy-time uncertainty statements depend on the observable, state evolution, and definition of characteristic time.

## Causality and paradoxes
A rule such as `P=0` for a paradox is a modeling axiom, not a derived law of physics. A fixed-point consistency rule can be studied as a mathematical model, but its physical status must be stated separately.

## Required audit record per equation
- Equation and source/reference
- Definitions and SI units
- Assumptions and domain
- Derivation or citation
- Test cases and limiting behavior
- Classification: established / active research / toy model / speculative / fiction
