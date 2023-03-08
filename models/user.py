#!/usr/bin/env python3
""" A User class """
from models.base_model import BaseModel


class User(BaseModel):
    """ A class User that inherits from BaseModel """
    def __init__(self):
        """Initializes the User Class"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
