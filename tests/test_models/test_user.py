#!/usr/bin/python3
"""This module contains the class TestUser"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Contains tests for the class User"""
    def test_attributes(self):
        """Test if all attributes are present"""
        u = User()
        self.assertTrue(hasattr(u, "email"))
        self.assertTrue(hasattr(u, "password"))
        self.assertTrue(hasattr(u, "first_name"))
        self.assertTrue(hasattr(u, "last_name"))

    def test_email(self):
        """Test if attributes are of correct type"""
        u = User()
        self.assertTrue(type(u.email), str)

    def test_password(self):
        u = User()
        self.assertTrue(type(u.password), str)

    def test_first_name(self):
        u = User()
        self.assertTrue(type(u.first_name), str)

    def test_last_name(self):
        u = User()
        self.assertTrue(type(u.last_name), str)
