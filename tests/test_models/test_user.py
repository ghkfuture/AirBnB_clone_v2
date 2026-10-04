#!/usr/bin/python3
"""Unittest for User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test case for User"""

    def test_instantiation(self):
        """Test instantiation of User"""
        obj = User()
        self.assertTrue(hasattr(obj, "id"))

    def test_to_dict(self):
        """Test to_dict method"""
        obj = User()
        d = obj.to_dict()
        self.assertEqual(d["__class__"], "User")


if __name__ == "__main__":
    unittest.main()
