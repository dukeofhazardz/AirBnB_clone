#!/usr/bin/env python3
"""A BaseModel Class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ A class that defines all common attributes/methods
        for other classes:"""
    def __init__(self, *args, **kwargs):
        """ Initializes the BaseModel class """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.name = ""
        self.my_number = None

        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.now().strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """ Updates the public instance attribute updated_at
            with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values
            of __dict__ of the instance: """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """ Returns the description of the BaseModel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
