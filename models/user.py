#!/usr/bin/env python3
""" Implements the user model"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits data from the BaseModel class and add's users
    functionalities

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
