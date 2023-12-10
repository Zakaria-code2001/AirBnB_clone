#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """User representaions that inherits from base model"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
