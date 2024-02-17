#!/usr/bin/python3

"""

"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertEqual(my_model.created_at, my_model.updated_at)

    def test_save_method(self):
        """
        Test if the save method updates the updated_at attribute
        """
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_str_representation(self):
        """
        Test if the __str__ method produces the expected output
        """
        my_model = BaseModel()
        expected_output = f"[{my_model.__class__.__name__}] ({my_model.id}) {my_model.__dict__}"

        self.assertEqual(str(my_model), expected_output)

    def test_to_dict_method(self):
        """
        Test if the to_dict method returns the expected dictionary
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class__"], "BaseModel")
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(
            my_model_dict["created_at"], my_model.created_at.isoformat()
        )
        self.assertEqual(
            my_model_dict["updated_at"], my_model.updated_at.isoformat()
        )


if __name__ == "__main__":
    unittest.main()
