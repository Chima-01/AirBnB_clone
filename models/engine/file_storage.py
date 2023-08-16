#!/usr/bin/python3
"""import relevant modules"""

import json
import os.path
from models.base_model import BaseModel 
from models.user import User
""" class FileStorage serializes instances to a JSON file
    and deserializes JSON file to instances """


class FileStorage:
    """ Initialize a private class attribute """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns private attribute object """
        return self.__objects

    def new(self, obj):
        """ makes key with obj class and id """
        ob_name = type(obj).__name__
        key = "{}.{}".format(ob_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serialize objects to json file """
        dict_json = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict_json, f)

    def reload(self):
        """ reaads from json file """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls_d = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_d)(**obj))
            return
