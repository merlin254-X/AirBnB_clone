#!/usr/bin/python3
"""
Module for FileStorage unittest
"""

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model.id = "123"
        self.file_storage.new(self.base_model)

    def tearDown(self):
        self.file_storage._FileStorage__objects = {}

    def test_all_returns_empty_dict(self):
        with patch('models.engine.file_storage.FileStorage._FileStorage__objects', {}):
            result = self.file_storage.all()
            self.assertIsInstance(result, dict)
            self.assertEqual(result, {})

    def test_all_returns_dict_with_objects(self):
        with patch('models.engine.file_storage.FileStorage._FileStorage__objects',
                   {'BaseModel.123': self.base_model}):
            result = self.file_storage.all()
            self.assertIsInstance(result, dict)
            self.assertEqual(result, {'BaseModel.123': self.base_model})


if __name__ == '__main__':
    unittest.main()

