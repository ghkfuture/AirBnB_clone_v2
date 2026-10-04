#!/usr/bin/python3
"""Unittest for City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test case for City"""

    def test_instantiation(self):
        """Test instantiation of City"""
        obj = City()
        self.assertTrue(hasattr(obj, "id"))

    def test_to_dict(self):
        """Test to_dict method"""
        obj = City()
        d = obj.to_dict()
        self.assertEqual(d["__class__"], "City")


if __name__ == "__main__":
    unittest.main()
