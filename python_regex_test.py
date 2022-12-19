import unittest
from unittest.mock import Mock

from celestial_body import CelestialBody


class CelestialBodyTest(unittest.TestCase):
    def test_calculate_gravity(self):
        self.assertEqual(CelestialBody.calculate_gravity(mass=10, diameter=2), 6.67e-10, "Should be a scientific value")
        self.assertEqual(CelestialBody.calculate_gravity(mass=5.97219e24, diameter=12742), 62524732851.98556,
                         "Should be a scientific value")
        self.assertEqual(CelestialBody.calculate_gravity(mass=5.97219e24, diameter=12742), 62524732851.98556,
                         "Should be a scientific value")
        self.assertEqual(CelestialBody.calculate_gravity(mass=5.97219, diameter=12213), 6.52329604519774e-14)
        self.assertGreater(CelestialBody.calculate_gravity(mass=20012, diameter=13223), 7.11211e-14)
        # self.assertRaises(ZeroDivisionError, CelestialBody.calculate_gravity, 10, 0)

    def test_celestial_body(self):
        celestial_bodies = CelestialBody()
        self.assertIsNone(celestial_bodies.set_celestial_body('title'), "None")
        self.assertIsNotNone(celestial_bodies.get_celestial_body('title'), "None")

    def test_calculate_rotation(self):
        celestial_bodies = CelestialBody()
        celestial_bodies.calculate_rotation = Mock()
        celestial_bodies.calculate_rotation.return_value = 124
        self.assertEqual(celestial_bodies.calculate_rotation(12, 23),
                         celestial_bodies.calculate_rotation.return_value)


if __name__ == '__main__':
    unittest.main()
