#!/usr/bin/python3
"""A unittest module for console.py"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
import models


class TestConsole(unittest.TestCase):
    """Test the HBNBCommand console"""

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            with self.assertRaises(SystemExit):
                HBNBCommand().onecmd("quit")

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            with self.assertRaises(SystemExit):
                HBNBCommand().onecmd("EOF")

    def test_emptyline(self):
        """Test emptyline"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), "")

    def test_create_missing_class(self):
        """Test create without class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        """Test create with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_class(self):
        """Test show without class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_invalid_class(self):
        """Test show with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        """Test show without id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_missing_class(self):
        """Test destroy without class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_all_invalid_class(self):
        """Test all with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")


if __name__ == "__main__":
    unittest.main()
