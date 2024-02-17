#!/usr/bin/python3
"""
class BaseModel that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Assign a unique ID using uuid.uuid4()
        """
        self.id = str(uuid.uuid4())
        """
        Assign the current datetime to created_at and updated_at
        """
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f')
                        setattr(self, key, value)
                else:
                    models.storage.new(self)

    def save(self):

        """
        Update the updated_at attribute with the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """
        Custom string representation
        """
        class_name = self.__class__.__name__
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
        Create a dictionary representation of the instance
        """
        instance_dict = self.__dict__.copy()

        """
        Add the __class__ key with the class name
        """
        instance_dict["__class__"] = self.__class__.__name__

        """
        Convert created_at and updated_at to ISO format strings
        """

        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key, value in my_model_json.items():
        print(f"\t{key}: ({type(value)}) - {value}")

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
