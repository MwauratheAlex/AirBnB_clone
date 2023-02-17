#!/usr/bin/python3
""" This module contains the class TestState"""
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
    """Contains tests for the class State"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_has_attributes(self):
        s = State()
        self.assertTrue(hasattr(s, "name"))

    def test_name(self):
        s = State()
        self.assertEqual(type(s.name), str)
