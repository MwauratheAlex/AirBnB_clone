#!/usr/bin/python3
""" This module contains the class City """

from models.base_model import BaseModel


class City(BaseModel):
    """ Represents a city """
    state_id = ""
    name = ""
