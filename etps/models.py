"""Small, transparent numerical models. These are not time-machine simulations."""
import math

C_M_S = 299_792_458.0
G_SI = 6.67430e-11

def lorentz_gamma(beta: float) -> float:
    """Lorentz factor for speed v=beta*c; require |beta| < 1."""
    if not math.isfinite(beta) or abs(beta) >= 1:
        raise ValueError("beta must be finite and satisfy |beta| < 1")
    return 1.0 / math.sqrt(1.0 - beta * beta)

def proper_time_for_inertial_trip(coordinate_seconds: float, beta: float) -> float:
    """Proper time for constant-speed inertial motion in flat spacetime."""
    if not math.isfinite(coordinate_seconds) or coordinate_seconds < 0:
        raise ValueError("coordinate_seconds must be finite and non-negative")
    return coordinate_seconds / lorentz_gamma(beta)

def schwarzschild_static_clock_ratio(radius_m: float, mass_kg: float) -> float:
    """dτ/dt for a static clock outside a non-rotating spherical mass.

    Valid only for r > 2GM/c² and idealized Schwarzschild exterior conditions.
    """
    if not (math.isfinite(radius_m) and math.isfinite(mass_kg)) or radius_m <= 0 or mass_kg <= 0:
        raise ValueError("radius and mass must be finite and positive")
    rs = 2.0 * G_SI * mass_kg / (C_M_S * C_M_S)
    if radius_m <= rs:
        raise ValueError("static Schwarzschild observer requires r > Schwarzschild radius")
    return math.sqrt(1.0 - rs / radius_m)

def mass_energy_joules(mass_kg: float) -> float:
    if not math.isfinite(mass_kg) or mass_kg < 0:
        raise ValueError("mass_kg must be finite and non-negative")
    return mass_kg * C_M_S**2
