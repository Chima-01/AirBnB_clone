#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """User class
    Args:
        email (string): email address of user
        password (string): user password
        first_name (string): user first_name
        last_name (string): user last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instance of user"""
        super().__init__(*args, **kwargs)
