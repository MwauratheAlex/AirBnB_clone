#!/usr/bin/python3
""" This module contains the tests for BaseModel """

from datetime import datetime
import unittest
import models.base_model
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Unittest for BaseModel """
    def test_module_docstring(self):
        """ Tests if module has docstring """
        self.assertTrue(len(models.base_model.__doc__) > 1)

    def test_class_docstring(self):
        """ Test if class has documentation """
        self.assertTrue(len(BaseModel.__doc__) > 1)

    def test_func_docstring(self):
        """ Test if functions are documented """
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_attributes(self):
        """ Test if attributes are present """
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_attr_types(self):
        """ Test if attributes are of correct type """
        b = BaseModel()
        self.assertTrue(type(b.id) is str)
        self.assertTrue(type(b.created_at) is datetime)
        self.assertTrue(type(b.updated_at) is datetime)

    def test_unique_id(self):
        """ Test if ids are unique """
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def test_print(self):
        a = BaseModel()
        self.assertEqual(str(a),
                         "[BaseModel] ({}) {}".format(a.id, a.__dict__))


if __name__ == "__main__":
    unittest.main()
