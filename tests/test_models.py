import unittest, math
from etps.models import lorentz_gamma, proper_time_for_inertial_trip, schwarzschild_static_clock_ratio, mass_energy_joules

class ModelTests(unittest.TestCase):
    def test_gamma_rest(self): self.assertAlmostEqual(lorentz_gamma(0), 1)
    def test_gamma_point_eight(self): self.assertAlmostEqual(lorentz_gamma(.8), 5/3)
    def test_proper_time(self): self.assertAlmostEqual(proper_time_for_inertial_trip(10, .8), 6)
    def test_invalid_speed(self):
        with self.assertRaises(ValueError): lorentz_gamma(1)
    def test_invalid_duration(self):
        with self.assertRaises(ValueError): proper_time_for_inertial_trip(-1, 0)
    def test_schwarzschild_ratio_below_one(self):
        self.assertGreater(schwarzschild_static_clock_ratio(1e7, 5.972e24), 0)
        self.assertLess(schwarzschild_static_clock_ratio(1e7, 5.972e24), 1)
    def test_schwarzschild_inside_radius_rejected(self):
        with self.assertRaises(ValueError): schwarzschild_static_clock_ratio(1, 1e30)
    def test_mass_energy(self): self.assertAlmostEqual(mass_energy_joules(1), 299792458**2)
if __name__ == "__main__": unittest.main()
