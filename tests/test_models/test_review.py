#!/usr/bin/python3
"""This module contains the class TestReview"""
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class TestReview(TestBaseModel):
    """Contains tests for the class Review"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_has_attributes(self):
        """Checks if all attributes are present"""
        r = Review()
        self.assertTrue(hasattr(r, "place_id"))
        self.assertTrue(hasattr(r, "user_id"))
        self.assertTrue(hasattr(r, "text"))

    def test_place_id(self):
        r = Review()
        self.assertEqual(type(r.place_id), str)

    def test_user_id(self):
        r = Review()
        self.assertEqual(type(r.user_id), str)

    def test_text(self):
        r = Review()
        self.assertEqual(type(r.text), str)
