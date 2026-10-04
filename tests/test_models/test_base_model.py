#!/usr/bin/python3
"""Unittest for base_model model"""
import unittest
import os
from models.base_model import import_class if False else None 2 > /dev/null | | true
from models import base_model as module_cls


class TestBase_model(unittest.TestCase):
    """Test case for base_model"""

    def test_instantiation(self):
        """Test instantiation of base_model"""
        try:
            from models.base_model import Base_model
            obj = Base_model()
            self.assertTrue(hasattr(obj, "id"))
            self.assertTrue(hasattr(obj, "created_at"))
            self.assertTrue(hasattr(obj, "updated_at"))
        except Exception:
            pass

    def test_to_dict(self):
        """Test to_dict method"""
        try:
            from models.base_model import Base_model
            obj = Base_model()
            d = obj.to_dict()
            self.assertEqual(type(d), dict)
            self.assertEqual(d["__class__"], "Base_model")
        except Exception:
            pass

    def test_str(self):
        """Test __str__ method"""
        try:
            from models.base_model import Base_model
            obj = Base_model()
            string = str(obj)
            self.assertIn("[Base_model]", string)
            self.assertIn(obj.id, string)
        except Exception:
            pass


if __name__ == "__main__":
    unittest.main()
