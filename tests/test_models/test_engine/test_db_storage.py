#!/usr/bin/python3
"""
Contains the TestDBStorageDocs classes
"""

import unittest
import os
import models
from models.engine import db_storage
from models.state import State
from models.city import City


class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db',
        "not testing db storage"
    )
    def test_all_returns_dict(self):
        """Test that all returns a dictionary"""
        self.assertIsInstance(models.storage.all(), dict)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db',
        "not testing db storage"
    )
    def test_new(self):
        """Test that new adds an object to the database"""
        state = State(name="California")
        models.storage.new(state)
        models.storage.save()
        self.assertIn(state, models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
