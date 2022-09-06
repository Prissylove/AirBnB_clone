#!/usr/bin/env python3
"""
    Test suite for console.py
"""

import os
import unittest
from models import storage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    """
        Tests the HBNB Command Interpreter
    """
    
    def test_emptyline(self):
        HBNBCommand().onecmd("")
        
    def test_do_quit(self):
        self.assertTrue(HBNBCommand().onecmd("quit"))
        
    def test_do_EOF(self):
        self.assertTrue(HBNBCommand().onecmd("EOF"))
        
class TestHBNBCommand_errors(unittest.TestCase):
    """
        Test cases for errors
    """
    
    def test_create_missing_class(self):
        e_string = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(e_string, obtained.getvalue().strip())
            
    def test_create_invalid_class(self):
        e_string = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("create")
            self.assertEqual(e_string, obtained.getvalue().strip())
            
    def test_show_missing_class(self):
        e_string = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as obtained:
            HBNBCommand().onecmd("show")
            self.assertEqual(e_string, obtained.getvalue().strip())
            
    