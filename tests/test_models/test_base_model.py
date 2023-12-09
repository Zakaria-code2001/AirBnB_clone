#!/usr/bin/python3

"""this module contains test cases for the base_model base class
"""



import unittest
from datetime import datetime
from uuid import uuid4
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """class that handles the methods with testcases for the basemodel class attributes"""
    
    def setUp(self):
        """setup of an instance of the base class"""
        
        self.item = BaseModel()

    def test_instance_creation(self):
        """method tests if instance has been generated successfully"""
        
        self.assertIsInstance(self.item, BaseModel)

    def test_id(self):
        """method to test the type of id - is it a str and uuid"""
        
        self.assertIsInstance(self.item.id, str)
        self.assertEqual(uuid4(self.item.id).version, 4)

    def test_created_at(self):
        """method that tests the type of created_at and if its set to current time"""
        
        self.assertIsInstance(self.item.created_at, datetime)
        self.assertAlmostEqual(self.item.created_at, datetime.now(), delta=datetime.timedelta(seconds=1))

    def test_updated_at(self):
        """method tests if updated at is a datetime object, and if it is equal
        to created at initially"""

        self.assertIsInstance(self.item.updated_at, datetime)
        self.assertEqual(self.item.updated_at, self.item.created_at)

    def test_updated_at(self):
        """checks if updated at time/day stamp changes when an update is made"""
        
        old_updated_at = self.item.updated_at
        self.item.update()

        self.assertNotEqual(old_updated_at, self.item.updated_at)
        self.assertGreater(self.item.updated_at, old_updated_at)

    def test_str(self):
        """method tests whether __str__ return output is as expected"""

        pass

    

if __name__ == "__main__":
    unittest.main()
