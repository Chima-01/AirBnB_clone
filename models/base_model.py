#!/usr/bin/python3
import datetime
import uuid
"""Defines Base Model class"""


class BaseModel:
    """Base model class
    
    Args:
        id (str): unique user id
        created_at (datetime obj): date account created
        updated_at (datetime obj): dtae account updated
    """

    def __init__(self, *args, **kwargs): #**kwargs
        """Creates instance of base model (constructor)"""
        if len(kwargs) != 0:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for (key, value) in kwargs.items():
                
        else:
            self.id = str(uuid.uuid4())
            #creates instance of datetime object
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
        """Return dictionary of object (added strings to dict then return dict)"""
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__': self.__class__.name,
                           'created_at': self.created_at.isoformat(),
                           'updated_at': self.updated_at.isoformat()})
        return dictionary
