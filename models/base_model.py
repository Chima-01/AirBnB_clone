#!/usr/bin/python3
from datetime import datetime
import uuid
"""Defines Base Model class"""


class BaseModel:
    """
    Attributes:
        args: This particular attribut will be unused in basemodel
        kwargs(dict): This updates an instance of basemodel according to the
                      key, value argument provided in kwargs
        id (str): unique user id
    """

    def __init__(self, *args, **kwargs):
        """Creates instance of base model (constructor)"""
        if len(kwargs) != 0:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"

            if "created_at" in kwargs:
                c_time = kwargs["created_at"]
                created_time = datetime.strptime(c_time, time_format)
                kwargs["created_at"] = created_time

            if "update_at" in kwargs:
                u_time = kwargs["updated_at"]
                updated_time = datetime.strptime(u_time, time_format)
                kwargs["updated_at"] = updated_time

            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            """ Creates an id, time instance was created, and update
                if kwargs is empty"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Prints [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates public instance attribute 'updated_at' w curr datetime"""
        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        """Return dictionary representation of object"""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["id"] = self.id
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict
