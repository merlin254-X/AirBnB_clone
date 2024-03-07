#!/usr/bin/python3
"""
Module for serializing and deserializing data
"""

import os
import json
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class for serializing/deserializing instances
    to/from JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as json_file:
            json.dump(json_dict, json_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)

                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    module_name = class_name.capitalize()

                    try:
                        cls = eval(class_name)
                        instance = cls(**value)
                        self.__objects[key] = instance
                    except AttributeError:
                        pass
