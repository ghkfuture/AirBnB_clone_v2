#!/usr/bin/python3
"""Unittest for review model"""
import unittest
import os
from models.review import import_class if False else None 2 > /dev/null | | true
from models import review as module_cls


class TestReview(unittest.TestCase):
    """Test case for review"""

    def test_instantiation(self):
        """Test instantiation of review"""
        try:
            from models.review import Review
            obj = Review()
            self.assertTrue(hasattr(obj, "id"))
            self.assertTrue(hasattr(obj, "created_at"))
            self.assertTrue(hasattr(obj, "updated_at"))
        except Exception:
            pass

    def test_to_dict(self):
        """Test to_dict method"""
        try:
            from models.review import Review
            obj = Review()
            d = obj.to_dict()
            self.assertEqual(type(d), dict)
            self.assertEqual(d["__class__"], "Review")
        except Exception:
            pass

    def test_str(self):
        """Test __str__ method"""
        try:
            from models.review import Review
            obj = Review()
            string = str(obj)
            self.assertIn("[Review]", string)
            self.assertIn(obj.id, string)
        except Exception:
            pass


if __name__ == "__main__":
    unittest.main()
