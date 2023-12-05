## A unit test verifies that one specific aspect of a function's behavior is correct 
##A test case is a colleciton of unit tests that together prove that a funciton behaves as it's suppoed to, within the full rnage of situations you expect it to handle 
##full coverage includes a full range of unit tests coering all the possible ways you can use a function 

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    def test_first_last_name(self):
        """do names like 'janis sophia joplin work?"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin') #assert method verify that a result you received matches the reult you expect to receive 

    def test_first_last_middle(self):
        """do names with middle name work"""
        formatted_name = get_formatted_name('Eric','Banavong', 'Robert')
        self.assertEqual(formatted_name, 'Eric Robert Banavong')

if __name__ == '__main__':
    unittest.main() 