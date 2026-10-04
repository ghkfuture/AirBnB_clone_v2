#!/usr/bin/python3
"""Unittest for State class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test case for State"""

    def test_instantiation(self):
        """Test instantiation of State"""
        obj = State()
        self.assertTrue(hasattr(obj, "id"))

    def test_to_dict(self):
        """Test to_dict method"""
        obj = State()
        d = obj.to_dict()
        self.assertEqual(d["__class__"], "State")


if __name__ == "__main__":
    unittest.main()
