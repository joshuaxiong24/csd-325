# Joshua Xiong / 11/26/2026 / Module 7.2 Assignment

import unittest
from city_functions import city_country


class CityFunctionsTestCase(unittest.TestCase):
    """Tests for city_functions.py."""

    def test_city_country(self):
        """Does a city and country like 'Santiago, Chile' format correctly?"""
        formatted = city_country("santiago", "chile")
        self.assertEqual(formatted, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()
