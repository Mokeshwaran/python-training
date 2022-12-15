import unittest

from python_regex import CelestialBody


class CelestialBodyTest(unittest.TestCase):
    def test_calculate_gravity(self):
        self.assertEqual(CelestialBody.calculate_gravity(mass=10, diameter=2), 6.67e-10, "Should be a scientific value")
        self.assertEqual(CelestialBody.calculate_gravity(mass=5.97219e24, diameter=12742), 62524732851.98556,
                         "Should be a scientific value")
        self.assertEqual(CelestialBody.calculate_gravity(mass=5.97219e24, diameter=12742), 62524732851.98556,
                         "Should be a scientific value")
        self.assertEqual(CelestialBody.calculate_gravity(mass=5.97219, diameter=12213), 6.52329604519774e-14)


if __name__ == '__main__':
    unittest.main()
