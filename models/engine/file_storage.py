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
        """ Makes key with obj class and id """
        ob_name = obj.__class.__name__
        key = "{}.{}".format(ob_name, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serialize objects to json file """
        serialized_dict = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(serialized_dict))

    def reload(self):
        """Deserialize json file to objects if file exists"""
        try:
            with open(self.__file_path, 'r') as file:
                json_text = json.load(file)
                for (key, value) in json_text.items():
                    class = value["__class__"]
                    del value["__class__"]
                    objects = eval(value["__class__"] + "(**value)")
                    objects = self.__objects[key]
        except FileNotFoundException:
            return
