#!/usr/bin/python3
"""Test for the console module"""

import unittest
from io import StringIO
from console import HBNBCommand
import sys
from os import getenv


class TestConsole(unittest.TestCase):
    """Class to test the behavior of the console"""

    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()

    def test_docstrings_existence(self):
        """Check if all methods have docstrings"""
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    @classmethod
    def get_output(cls):
        """Get the output from stdout"""
        temp_out = StringIO()
        sys.stdout = temp_out
        return temp_out.getvalue()

    def test_create_errors(self):
        """Test error cases for the create command"""
        temp_out = StringIO()
        sys.stdout = temp_out

        self.console.onecmd("create")
        self.assertEqual(temp_out.getvalue(), '** class name missing **\n')
        temp_out.close()

        temp_out = StringIO()
        sys.stdout = temp_out
        HBNBCommand().do_create("base")
        self.assertEqual(temp_out.getvalue(), '** class doesn\'t exist **\n')
        temp_out.close()

        temp_out = StringIO()
        sys.stdout = temp_out
        if getenv("HBNB_TYPE_STORAGE") != "db":
            HBNBCommand().do_create("BaseModel")
            self.assertTrue(temp_out.getvalue() != "")
        temp_out.close()
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
