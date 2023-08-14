#!/usr/bin/python3
"""Defines Place class that inherits from Base class"""
from .base_model import BaseModel


class Place(BaseModel):
    """Place class
    Args:
        city_id (string): city id
        user_id (string): user id
        name (string): name of city
        description (string): description of place
        number_rooms (integer): number of rooms
        number_bathrooms (integer): number of bathrooms
        max_guest (integer): maximum number of guests allowed
        price_by_night (integer): nightly rate
        latitude (float): latitudinal position
        longitude (float): longitudinal position
        amenity_ids (str list): list of amenity.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Creates new instance of place"""
        super().__init__(*args, **kwargs)
