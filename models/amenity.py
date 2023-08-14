#!/usr/bin/python3
"""Defines Amenity class that inherits from Base class"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class
    Args:
        name (string): name of amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instance of amenity"""
        super().__init__(*args, **kwargs)
