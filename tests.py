import unittest
from main_console import *
from register import *
from login import *
from admin import *

'''Couldnot write all the test cases due to time constraints'''
class TestRegister(unittest.TestCase):
    def test_register(self):
        user = User('John', 'john@gmail.com', 'Python')
        self.assertEqual(user.register(), 'John has been registered')
    
