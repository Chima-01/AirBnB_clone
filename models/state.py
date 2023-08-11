#!/usr/bin/python3
"""Defines State class that inherits from Base class"""
from .base_model import BaseModel


class State(BaseModel):
    """State class
    Args:
        name (string): name of state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instance of state"""
        super().__init__(*args, **kwargs)
