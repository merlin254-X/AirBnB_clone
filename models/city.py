#!/usr/bin/python3
"""
Module for the City class.
"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    City class for storing city information.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
