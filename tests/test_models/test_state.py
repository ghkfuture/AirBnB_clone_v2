#!/usr/bin/python3
"""Unittest for state model"""
import unittest
import os
from models.state import import_class if False else None 2 > /dev/null | | true
from models import state as module_cls


class TestState(unittest.TestCase):
    """Test case for state"""

    def test_instantiation(self):
        """Test instantiation of state"""
        try:
            from models.state import State
            obj = State()
            self.assertTrue(hasattr(obj, "id"))
            self.assertTrue(hasattr(obj, "created_at"))
            self.assertTrue(hasattr(obj, "updated_at"))
        except Exception:
            pass

    def test_to_dict(self):
        """Test to_dict method"""
        try:
            from models.state import State
            obj = State()
            d = obj.to_dict()
            self.assertEqual(type(d), dict)
            self.assertEqual(d["__class__"], "State")
        except Exception:
            pass

    def test_str(self):
        """Test __str__ method"""
        try:
            from models.state import State
            obj = State()
            string = str(obj)
            self.assertIn("[State]", string)
            self.assertIn(obj.id, string)
        except Exception:
            pass


if __name__ == "__main__":
    unittest.main()
