#!/usr/bin/python3
#a class BaseModel that defines all common attributes/methods for other classes

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    designing the baseModel Class with the instance attributes initialization
    """

    def __init__(self):
        """
        creating a public instance attribute with a random id generate by uuid4().
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """
        This Method is used to update_at attribute with the current date and time using the datetime module
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        this method get the values which are of datetime object type and  convert them to string objects in ISO format
        """
        dictFormat = {}
        dictFormat["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, type(datetime)):
                dictFormat[key] = value.isoformat()
            else:
                dictFormat[key] = value
        return dictFormat

    def __str__(self):
        """
        We are using the __str__ method to return a human readable or informal string representation of an object.
        """
        return f'{[self.__class__.__name__]} {(self.id)} {self.__dict__}'
