#!/usr/bin/env python3
"""
    Contains the module that defines the amenity entity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Describes the Amenity class which inherits the BaseModel
        and adds a name
    """
    name = ""
