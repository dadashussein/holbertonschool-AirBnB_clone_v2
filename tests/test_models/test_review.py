#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review
        self.review1 = Review(place_id="eqer-5678-asdf-1234",
                              user_id="qwer-5678-asdf-1234",
                              text="This place is great!")

    def test_place_id(self):
        """ """
        self.assertEqual(type(self.review1.place_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(self.review1.user_id), str)

    def test_text(self):
        """ """
        self.assertEqual(type(self.review1.text), str)
