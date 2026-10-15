# Formula notes and derivation sketches

## Inertial time dilation
In Minkowski spacetime with signature (−,+,+,+), the interval for motion along one spatial axis is c²dτ²=c²dt²−dx². With constant coordinate speed v=dx/dt, dτ=dt√(1−v²/c²). Integrating over a constant-speed segment yields Δτ=Δt√(1−β²)=Δt/γ. For accelerated paths, integrate the local expression along each segment; do not apply one constant β to the whole path unless it is actually constant.

## Schwarzschild static clock
For the Schwarzschild exterior metric, the time component is g_tt=−(1−2GM/(rc²)) when the time coordinate is measured in seconds and the metric is written with consistent SI factors. A static observer has fixed spatial coordinates, so the proper-time relation reduces to dτ/dt=√(1−2GM/(rc²)). The formula requires a static worldline outside r_s and the idealized non-rotating spherical geometry.

## Mass-energy
Rest energy is E₀=mc². Relativistic total energy and momentum satisfy E²=p²c²+m²c⁴. Use the second relation when kinetic energy or momentum is material to the question.

## Density operator checks
A valid density matrix is Hermitian, positive semidefinite, and trace one. For a pure state ρ²=ρ and Tr(ρ²)=1. For a maximally mixed state in dimension d, ρ=I/d and purity is 1/d. Numerical implementations should test Hermiticity, trace, and eigenvalue bounds within a stated tolerance.

## Numerical analysis
Use dimensionless parameters where possible. Test limits: β→0 should give γ→1; β→1⁻ should make γ grow without bound; r→∞ should make the Schwarzschild clock ratio approach 1. Reject invalid domains instead of silently returning NaN.
