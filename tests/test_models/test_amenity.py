#!/usr/bin/python3
"""Unittest for Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test case for Amenity"""

    def test_instantiation(self):
        """Test instantiation of Amenity"""
        obj = Amenity()
        self.assertTrue(hasattr(obj, "id"))

    def test_to_dict(self):
        """Test to_dict method"""
        obj = Amenity()
        d = obj.to_dict()
        self.assertEqual(d["__class__"], "Amenity")


if __name__ == "__main__":
    unittest.main()
