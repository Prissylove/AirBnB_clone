#!/usr/bin/env python3
"""
A module for testing the base model class
"""
import unittest
from datetime import datetime
from uuid import uuid4
import models

class TestBaseModel(unittest.TestCase):
    """
    The test suite for models.base_model
    """
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
