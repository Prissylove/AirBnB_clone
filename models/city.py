#!/usr/bin/env python3
"""
    Contains a module that has the city model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        Defines the city properties by inheriting the BaseModel and
        add a state id
    """
    name = ""
    state_id = ""
