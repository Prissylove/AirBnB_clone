#!/usr/bin/env python3
"""
    A module containing the state model
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
        State model is a child of the BaseModel
        it inherits all details and adds a name property
    """
    name = ""
