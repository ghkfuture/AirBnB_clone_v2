#!/usr/bin/python3
"""
Contains the TestFileStorageDocs classes
"""

from datetime import datetime
import inspect
import models
from models.engine import file_storage
from models.base_model import BaseModel
import json
import os
import unittest
FileStorage = file_storage.FileStorage
classes = {"BaseModel": BaseModel}


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test that all returns the __objects attr"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    def test_new(self):
        """Test that new adds an object to __objects"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage.all())
        FileStorage._FileStorage__objects = save

    def test_save_and_reload(self):
        """Test save creates file and reload loads objects"""
        bm = BaseModel()
        bm.save()
        key = "BaseModel.{}".format(bm.id)
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(key, new_storage.all())


if __name__ == "__main__":
    unittest.main()
