import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the FileStorage class.
    """
    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)


    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

    class TestFileStorage_methods(unittest.TestCase):
        """
        Unittests for testing methods of the FileStorage class.
        """
    def setUp(self):
        self.test_file == "test_file.json"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
            
