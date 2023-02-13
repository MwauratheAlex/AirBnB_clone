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
        key = "{}.{}".format(obj.to_dict()["__class__"], obj.to_dict()["id"])
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path """
        temp = {}
        for key, value in self.__objects.items():
            temp[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(temp))

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        classes = {
            "BaseModel" : BaseModel,
            "User" : User,
            "State" : State,
            "City" : City,
            "Amenity" : Amenity,
            "Place" : Place,
            "Review" : Review
            }
        temp = {}
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                temp = json.loads(f.read())
                for key, value in temp.items():
                    self.__objects[key] = classes[value["__class__"]](**value)
