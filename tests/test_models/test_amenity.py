#!/usr/bin/python3
"""This module contains the class TestAmenity"""
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    """Contains tests for the class Amenity"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_has_attr(self):
        """Check if all attributes are present"""
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))

    def test_name(self):
        """Checks if name type is correct"""
        a = Amenity()
        self.assertEqual(type(a.name), str)
