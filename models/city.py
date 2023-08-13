#!/usr/bin/python3
"""Defines City class that inherits from Base class"""
from .base_model import BaseModel
from .state import State


class City(BaseModel):
    """City class
    Args:
        state_id (string): state id
        name (string) = name of city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instance of city"""
        super().__init__(*args, **kwargs)
