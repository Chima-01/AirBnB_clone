#!/usr/bin/python3
import json
import os.path
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
        ob_name = obj.__class.__name__
        key = "{}.{}".format(ob_name, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serialize objects to json file """
