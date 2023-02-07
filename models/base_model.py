#!/usr/bin/python3
""" This module contains the BaseModel class """

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ BaseModel class
    defines all common attributes/methods for other classes """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ print: [<class name>] (<self.id>) <self.__dict__> """
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """  updates the public instance attribute
        updated_at with the current datetime """
        self.created_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance """
        class_dict = self.__dict__
        class_dict["__class__"] = self.__class__.__name__
        class_dict["created_at"] = class_dict["created_at"].isoformat()
        class_dict["updated_at"] = class_dict["updated_at"].isoformat()

        return class_dict
