#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place
        self.place1 = Place(city_id="asdf-1234-ghjk-5678",
                            user_id="qwer-5678-asdf-1234",
                            name="House of the Rising Sun",
                            description="A place to stay for the night.",
                            number_rooms=3,
                            number_bathrooms=4,
                            max_guest=15,
                            price_by_night=20,
                            latitude=12.4,
                            longtitude=14.12,
                            amenity_ids=[])

    def test_city_id(self):
        """ """
        self.assertEqual(type(self.place1.city_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(self.place1.user_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(self.place1.name), str)

    def test_description(self):
        """ """
        self.assertEqual(type(self.place1.description), str)

    def test_number_rooms(self):
        """ """
        self.assertEqual(type(self.place1.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        self.assertEqual(type(self.place1.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        self.assertEqual(type(self.place1.max_guest), int)

    def test_price_by_night(self):
        """ """
        self.assertEqual(type(self.place1.price_by_night), int)

    def test_latitude(self):
        """ """
        self.assertEqual(type(self.place1.latitude), float)

    def test_longitude(self):
        """ """
        self.assertEqual(type(self.place1.latitude), float)

    def test_amenity_ids(self):
        """ """
        self.assertEqual(type(self.place1.amenity_ids), list)
