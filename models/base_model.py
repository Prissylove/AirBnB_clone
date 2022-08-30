#!/usr/bin/env python3
""" Base model for console for HBnB"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This defines the class for the base of the hBnB project
       It has various properties to define the
    """
    def __init__(self, *args, **kwargs):
        """Init function for the BaseModel"""

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def save(self):
        """Save method updates the public instance attribute `updated_at` """
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns printable string representation of the rectangle"""
        string = "[{}] ({}) <{}>".format(type(self).__name__,
                                         self.id,
                                         self.__dict__)
