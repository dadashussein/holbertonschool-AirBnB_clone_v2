#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City
        self.city1 = City(state_id="CA",
                          name="San Francisco")

    def test_state_id(self):
        """ """
        self.assertEqual(type(self.city1.state_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(self.city1.name), str)
        self.assertEqual(self.city1.name, "San Francisco")
        self.city1.name = "Los Angeles"
        self.assertEqual(self.city1.name, "Los Angeles")
