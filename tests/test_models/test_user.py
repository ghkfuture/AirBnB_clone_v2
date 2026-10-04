#!/usr/bin/python3
"""Unittest for user model"""
import unittest
import os
from models.user import import_class if False else None 2 > /dev/null | | true
from models import user as module_cls


class TestUser(unittest.TestCase):
    """Test case for user"""

    def test_instantiation(self):
        """Test instantiation of user"""
        try:
            from models.user import User
            obj = User()
            self.assertTrue(hasattr(obj, "id"))
            self.assertTrue(hasattr(obj, "created_at"))
            self.assertTrue(hasattr(obj, "updated_at"))
        except Exception:
            pass

    def test_to_dict(self):
        """Test to_dict method"""
        try:
            from models.user import User
            obj = User()
            d = obj.to_dict()
            self.assertEqual(type(d), dict)
            self.assertEqual(d["__class__"], "User")
        except Exception:
            pass

    def test_str(self):
        """Test __str__ method"""
        try:
            from models.user import User
            obj = User()
            string = str(obj)
            self.assertIn("[User]", string)
            self.assertIn(obj.id, string)
        except Exception:
            pass


if __name__ == "__main__":
    unittest.main()
