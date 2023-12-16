import unittest
from employee import EmployeeInfo

class testEmployeeInfo(unittest.TestCase):

    def setUp(self):
        self.eric=('Eric','Banavong', 200000)

    def test_give_default_raise(self):
        self.eric.give_raise()
        self.assertEqual(self.eric.salary, 70000)
unittest.main()
    


