#!/usr/bin/python3
""" This module contains the class FileStorage"""

import json
import os
from os import path


class FileStorage:
    """ FileStorage class: serializes instances to a JSON file
    and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj["__class__"], obj["id"])
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path """
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                self.__objects = json.loads(f.read())
