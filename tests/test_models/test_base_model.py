#!/usr/bin/python3
"""Unittest for BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test case for BaseModel"""

    def test_instantiation(self):
        """Test instantiation of BaseModel"""
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))

    def test_to_dict(self):
        """Test to_dict method"""
        obj = BaseModel()
        d = obj.to_dict()
        self.assertEqual(type(d), dict)
        self.assertEqual(d["__class__"], "BaseModel")

    def test_str(self):
        """Test __str__ method"""
        obj = BaseModel()
        string = str(obj)
        self.assertIn("[BaseModel]", string)
        self.assertIn(obj.id, string)


if __name__ == "__main__":
    unittest.main()
