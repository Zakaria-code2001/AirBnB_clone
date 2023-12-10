#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class representation that inherits from a basemodel"""

    place_id = ""
    user_id = ""
    text = ""
