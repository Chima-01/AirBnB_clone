#!/usr/bin/python3
"""Defines Review class that inherits from Base class"""
from .base_model import BaseModel


class Review(BaseModel):
    """Review class

    Args:
        place_id (string): place id from Place class
        user_id (string) = user id from User class
        text (string): review text of place
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Creates new instance of Review"""
        super().__init__(*args, **kwargs)
