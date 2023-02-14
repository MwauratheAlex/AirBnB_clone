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

    def test_str(self):
        """ Test str """
        a = BaseModel()
        self.assertEqual(str(a),
                         "[BaseModel] ({}) {}".format(a.id, a.__dict__))

    def test_to_dict(self):
        """ Test to dict """
        b = BaseModel()
        class_dict = vars(b).copy()
        class_dict["__class__"] = "BaseModel"
        class_dict["created_at"] = class_dict["created_at"].isoformat()
        class_dict["updated_at"] = class_dict["updated_at"].isoformat()
        self.assertEqual(b.to_dict(), class_dict)

    def test_save(self):
        b = BaseModel()
        updated_at_f = b.updated_at
        b.save()
        updated_at_l = b.updated_at
        self.assertNotEqual(updated_at_f, updated_at_l)


if __name__ == "__main__":
    unittest.main()
