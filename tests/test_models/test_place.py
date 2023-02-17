#!/usr/bin/python3
"""This module contains the class TestPlace"""
from tests.test_models.test_base_model import TestBaseModel
from models.place import Place


class TestPlace(TestBaseModel):
    """Contains tests for the class Place"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_has_attr(self):
        """Check if all attributes are present"""
        p = Place()
        self.assertTrue(hasattr(p, "city_id"))
        self.assertTrue(hasattr(p, "user_id"))
        self.assertTrue(hasattr(p, "name"))
        self.assertTrue(hasattr(p, "description"))
        self.assertTrue(hasattr(p, "number_rooms"))
        self.assertTrue(hasattr(p, "number_bathrooms"))
        self.assertTrue(hasattr(p, "max_guest"))
        self.assertTrue(hasattr(p, "price_by_night"))
        self.assertTrue(hasattr(p, "latitude"))
        self.assertTrue(hasattr(p, "longitude"))
        self.assertTrue(hasattr(p, "amenity_ids"))

    def test_city_id(self):
        p = Place()
        self.assertEqual(type(p.city_id), str)

    def test_user_id(self):
        p = Place()
        self.assertEqual(type(p.user_id), str)

    def test_name(self):
        p = Place()
        self.assertEqual(type(p.name), str)

    def test_description(self):
        p = Place()
        self.assertEqual(type(p.description), str)

    def test_number_rooms(self):
        p = Place()
        self.assertEqual(type(p.number_rooms), int)

    def test_number_bathrooms(self):
        p = Place()
        self.assertEqual(type(p.number_bathrooms), int)

    def test_max_guest(self):
        p = Place()
        self.assertEqual(type(p.max_guest), int)

    def test_price_by_night(self):
        p = Place()
        self.assertEqual(type(p.price_by_night), int)

    def test_latitude(self):
        p = Place()
        self.assertEqual(type(p.latitude), float)

    def test_longitude(self):
        p = Place()
        self.assertEqual(type(p.longitude), float)

    def test_amenity_ids(self):
        p = Place()
        self.assertEqual(type(p.amenity_ids), list)
