#!/usr/bin/python3
""" This module contains the class TestFileStorage """
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
from os import path
from models import storage


class TestFileStorage(unittest.TestCase):
    """ Contains tests for the class FileStorage """
    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_module_doc(self):
        """ Tests if module is documented """
        self.assertTrue(len(models.engine.file_storage.__doc__) > 1)

    def test_class_doc(self):
        """ Tests if class is documented """
        self.assertTrue(len(FileStorage.__doc__) > 1)

    def test_func_doc(self):
        """ Tests if all functions are documented """
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_all(self):
        """ Tests the function all() """
        fs = FileStorage()
        self.assertTrue(type(fs.all()) is dict)

    def test_new(self):
        """ Tests the function new(obj) """
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        key = "BaseModel.{}".format(bm.id)
        self.assertTrue(key in fs.all())

    def test_save(self):
        """ Tests the function save() """
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        fs.save()
        self.assertTrue(path.exists("file.json"))
        with open("file.json", "r") as f:
            json = f.read()
            self.assertIn("BaseModel.{}".format(bm.id), json)

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()
