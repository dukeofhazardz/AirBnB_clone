#!/usr/bin/env python3
""" A FileStorage class """
import json
from models.base_model import BaseModel


class FileStorage:
    """ A class FileStorage that serializes instances to a
        JSON file and deserializes JSON file to instances:

        Attributes:
            __file_path (str): The name of the file to save objects to.
            __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        oc_name = obj.__class__.__name__
        self.__objects["{}.{}".format(oc_name, obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        json_data = {}
        for k, v in self.__objects.items():
            json_data[k] = v.to_dict()
        with open(self.__file_path,'w') as jsonf:
            json.dump(json_data, jsonf)

    def reload(self):
        """ Deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists ; otherwise, do nothing. If the file doesn’t
            exist, no exception should be raised) """
        try:
            with open(self.__file_path, 'r') as jsonf:
                obj_dict = json.load(jsonf)
                for obj in obj_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
