#!/usr/bin/env python3
"""
This contains the module definition for the file engine
"""

import json
from models.base_model import BaseModel

classes = {
    "BaseModel": BaseModel
}


class FileStorage:
    """
    Serializes the instance to JSON and
    deserializes JSON file to instance
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns self.__object which is a dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the `obj` with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        serializes `__objects` to the JSON file in `__file_path`
        """
        dict_storage = {}
        for k, v in self.__objects.items():
            dict_storage[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dict_storage, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        only if file exists
        """
        try:
            with open(self.__file_path, 'r') as f:
                jOb = json.load(f)

            for k in jOb:
                self.__objects[k] = classes[jOb[k]["__class__"]](**jOb[k])
        except IOError:
            pass
