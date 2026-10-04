#!/usr/bin/python3
"""Unittest for Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test case for Review"""

    def test_instantiation(self):
        """Test instantiation of Review"""
        obj = Review()
        self.assertTrue(hasattr(obj, "id"))

    def test_to_dict(self):
        """Test to_dict method"""
        obj = Review()
        d = obj.to_dict()
        self.assertEqual(d["__class__"], "Review")


if __name__ == "__main__":
    unittest.main()
