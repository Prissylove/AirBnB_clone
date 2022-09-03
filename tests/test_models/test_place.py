#!/usr/bin/env python3
"""
Test suite for the Place class of models.place
"""
import unittest
from models import place

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
        Test cases agains the place class
    """
    def setUp(self):
        self.place = Place()
        self.attr_list = ["name",
                          "user_id",
                          "city_id",
                          "description",
                          "number_bathrooms",
                          "max_guest",
                          "number_rooms",
                          "price_by_night",
                          "latitude",
                          "longitude",
                          "amenity_ids"]

    def test_attr_are_class_attr(self):
        for attr in self.attr_list:
            self.assertTrue(hasattr(Place, attr))

    def test_class_attr(self):
        self.assertIs(type(self.place.name), str)
        self.assertIs(type(self.place.city_id), str)
        self.assertIs(type(self.place.user_id), str)
        self.assertIs(type(self.place.description), str)
        self.assertIs(type(self.place.number_bathrooms), int)
        self.assertIs(type(self.place.max_guest), int)
        self.assertIs(type(self.place.number_rooms), int)
        self.assertIs(type(self.place.price_by_night), int)
        self.assertIs(type(self.place.latitude), float)
        self.assertIs(type(self.place.longitude), float)
        self.assertIs(type(self.place.amenity_ids), list)

        for attr in self.attr_list:
            self.assertFalse(bool(getattr(self.place, attr)))

    def test_place_obj_is_a_subclass(self):
        self.assertTrue(issubclass(type(self.place), BaseModel))
