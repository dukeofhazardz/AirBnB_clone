#!/usr/bin/python3
""" A Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ The Review class that inherits from BaseModel class

    Attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
