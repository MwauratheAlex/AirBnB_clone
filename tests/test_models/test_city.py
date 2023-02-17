#!/usr/bin/python3
"""Module contains class TestCity"""
from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class TestCity(TestBaseModel):
    """Contains test for class City"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_has_attributes(self):
        """Test if all attributes are present"""
        c = self.value()
        self.assertTrue(hasattr(c, "state_id"))
        self.assertTrue(hasattr(c, "name"))

    def test_attr_types(self):
        """Test if attributes are of correct type"""
        c = self.value()
        self.assertTrue(type(c.state_id), str)
        self.assertTrue(type(c.name), str)
