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
        return string

    def to_dict(self):
        """Returns diction representation of the object
        - only instance attributes would be returned
        - a key __class__ would be added to the new object
        - created_at and update_at would be converted to ISO format
        """
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                dict_1[k] = v
        return dict_1
