import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr1(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_repr2(self):
        loc = Location("SLO", 34.2+.1+.1+.1+.1+.1+.1+.1+.1+.1+.1+.1, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    # Add more tests!
    def test_eq1(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = 6
        self.assertNotEqual(loc1, loc2)

    def test_eq2(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertNotEqual(loc1, loc2)

    def test_eq3(self):
        loc1 = Location("Paris", 48.9, 2.4)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertEqual(loc1, loc2)

    def test_init(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.name, "SLO")
        self.assertEqual(loc.lat, 35.3)
        self.assertEqual(loc.lon, -120.7)

if __name__ == "__main__":
        unittest.main()
