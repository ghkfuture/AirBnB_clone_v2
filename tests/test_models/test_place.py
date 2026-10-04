#!/usr/bin/python3
"""Unittest for Place class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test case for Place"""

    def test_instantiation(self):
        """Test instantiation of Place"""
        obj = Place()
        self.assertTrue(hasattr(obj, "id"))

    def test_to_dict(self):
        """Test to_dict method"""
        obj = Place()
        d = obj.to_dict()
        self.assertEqual(d["__class__"], "Place")


if __name__ == "__main__":
    unittest.main()
