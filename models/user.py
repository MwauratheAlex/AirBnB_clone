#!/usr/bin/python3
""" This module contains the class User """

import BaseModel


class User(BaseModel):
    """ Represents a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
