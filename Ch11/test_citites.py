import unittest
from city_functions import get_city_name

class CityFunctionTestCase(unittest.TestCase):
    """test city function"""

    def test_city_country(self):
        """do city and country like New York, USA work"""
        formatted_city = get_city_name('los angeles', 'Usa')
        self.assertEqual(formatted_city, 'Los Angeles Usa')
    
    def test_city_population(self):
        """do city country and population work"""
        formatted_city_population = get_city_name('los angeles','Usa','4000000')
        self.assertEqual(formatted_city_population, 'Los Angeles Usa 4000000')
if __name__ == '__main__':
    unittest.main() 